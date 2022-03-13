const { src, dest, watch, series } = require("gulp"),
  concat = require("gulp-concat"),
  pug = require("gulp-pug"),
  sass = require("gulp-sass")(require("sass")),
  prefix = require("gulp-autoprefixer"),
  minify = require("gulp-clean-css"),
  terser = require("gulp-terser"),
  imagewebp = require("gulp-webp"),
  sourcemaps = require("gulp-sourcemaps");

// scss
function compilescss() {
  return src("../scss/*.scss")
    .pipe(sourcemaps.init())
    .pipe(sass())
    .pipe(prefix("last 2 versions"))
    .pipe(minify())
    .pipe(sourcemaps.write("../../static/maps/css"))
    .pipe(dest("../../static/css"));
}

//js [main]
function jsmin_main() {
  return src("../js/main/*.js")
    .pipe(sourcemaps.init())
    .pipe(concat("main.js"))
    .pipe(terser())
    .pipe(sourcemaps.write("../../maps/js"))
    .pipe(dest("../../static/js/main"));
}

//js [episode]
function jsmin_episode() {
  return src("../js/episode/*.js")
    .pipe(sourcemaps.init())
    .pipe(concat("main.js"))
    .pipe(terser())
    .pipe(sourcemaps.write("../../maps/js"))
    .pipe(dest("../../static/js/episode"));
}

//js [anime_info]
function jsmin_anime_info() {
  return src("../js/anime_info/*.js")
    .pipe(sourcemaps.init())
    .pipe(concat("main.js"))
    .pipe(terser())
    .pipe(sourcemaps.write("../../maps/js"))
    .pipe(dest("../../static/js/anime_info"));
}

//js [anime_list]
function jsmin_anime_list() {
  return src("../js/anime_list/*.js")
    .pipe(sourcemaps.init())
    .pipe(concat("main.js"))
    .pipe(terser())
    .pipe(sourcemaps.write("../../maps/js"))
    .pipe(dest("../../static/js/anime_list"));
}

//js [home]
function jsmin_home() {
  return src("../js/home/*.js")
    .pipe(sourcemaps.init())
    .pipe(concat("main.js"))
    .pipe(terser())
    .pipe(sourcemaps.write("../../maps/js"))
    .pipe(dest("../../static/js/home"));
}

//js [anime_movies]
function jsmin_anime_movies() {
  return src("../js/anime_movies/*.js")
    .pipe(sourcemaps.init())
    .pipe(concat("main.js"))
    .pipe(terser())
    .pipe(sourcemaps.write("../../maps/js"))
    .pipe(dest("../../static/js/anime_movies"));
}

//js [profile]
function jsmin_profile() {
  return src("../js/profile/*.js")
    .pipe(sourcemaps.init())
    .pipe(concat("main.js"))
    .pipe(terser())
    .pipe(sourcemaps.write("../../maps/js"))
    .pipe(dest("../../static/js/profile"));
}

//js [comments]
function jsmin_comments() {
  return src("../js/comments/*.js")
    .pipe(sourcemaps.init())
    .pipe(concat("main.js"))
    .pipe(terser())
    .pipe(sourcemaps.write("../../maps/js"))
    .pipe(dest("../../static/js/comments"));
}

// webp images
function webpImage() {
  return src("../img/**/*.{jpg, png}")
    .pipe(imagewebp())
    .pipe(dest("../../static/img"));
}

// create watchtask
function watchTask() {
  watch("../scss/**/*.scss", compilescss);
  watch("../img/**/*.{jpg, png}", webpImage);
  // js files
  watch("../js/main/**/*.js", jsmin_main);
  watch("../js/episode/**/*.js", jsmin_episode);
  watch("../js/anime_info/**/*.js", jsmin_anime_info);
  watch("../js/anime_list/**/*.js", jsmin_anime_list);
  watch("../js/home/**/*.js", jsmin_home);
  watch("../js/anime_movies/**/*.js", jsmin_anime_movies);
  watch("../js/profile/**/*.js", jsmin_profile);
  watch("../js/comments/**/*.js", jsmin_comments);
}

// default gulp
exports.default = series(compilescss, watchTask);
