const avatars = [
    'cat.png', 'chicken.png', 'duck.png', 'hen.png',
    'koala.png', 'meerkat.png', 'panda.png', 'rabbit.png',
    'sea-lion.png', 'shark.png', 'weasel.png'
];

function getAvatarUrl(userId) {
    const avatarIndex = userId % avatars.length;
    return new URL(`../assets/avatars/${avatars[avatarIndex]}`, import.meta.url).href;
}

export { getAvatarUrl };