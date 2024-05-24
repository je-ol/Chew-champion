<template>
  <div class="page-container h-[80vh] w-[100%] flex flex-col items-center mt-[80px]">
    <div class="center-container w-[60%] h-[100%] my-10">
      <div class="blog-info self-start">
        <input
          type="text"
          placeholder="Enter a Blog title"
          v-model="blogTitle"
          class="w-[50%] py-1 px-2 border-b-2 border-black bg-inherit"
        />
        <div class="upload-photo flex my-4">
          <label for="blog-photo">Upload a cover photo
            <input
              type="file"
              ref="blogPhoto"
              id="blog-photo"
              accept=".png, .jpg, .jpeg"
              @change="handleFileUpload"
            />
          </label>
        </div>
      </div>
      <div class="editor h-[50%] w-[100%]">
        <textarea 
          v-model="blogHTML"
          placeholder="Enter your blog content"
          class="w-full h-full p-2 border-2 border-black"
        ></textarea>
      </div>
      <div class="blog-actions flex gap-5 mt-16 text-white">
        <button
          class="bg-[#758bfd] px-4 py-2 rounded-sm font-bold"
          @click="publishBlog"
        >Publish Blog</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  name: "NewPost",
  data() {
    return {
      blogTitle: "",
      blogHTML: "",
      blogPhoto: null,
      error: null,
      errorMsg: null,
    };
  },
  methods: {
  handleFileUpload(event) {
    this.blogPhoto = event.target.files[0];
  },
  async publishBlog() {
  console.log("Blog Title:", this.blogTitle);
  console.log("Blog HTML:", this.blogHTML);

    try {
      const formData = new FormData();

      formData.append("image", this.blogPhoto), {
        type: 'file'
      };
      formData.append("title", this.blogTitle), {
        type: 'text'
      
      };
      formData.append("content", this.blogHTML), {
        type: 'text'
      };

/*       for (const [key, value] of formData.entries()) {
      console.log(`${key}:`, value);
      } */

    // Send formData with both image and JSON data
      const response = await axios.post("/posts/upload_image/", formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: `token ${localStorage.getItem('token')}`
        }
      });

      if (response.status === 200 || response.status === 201) {
        alert("Blog published successfully");
        this.$router.push("/");
      } else {
        throw new Error('Failed to publish blog');
      }
    } catch (error) {
      console.log(error);
      this.error = true;
      this.errorMsg = "An error occurred while publishing the blog";
    }
  }
},
};
</script>
