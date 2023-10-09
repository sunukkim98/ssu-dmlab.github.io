# Manual for the website of DMLAB @ SSU

## Installation
To run this website on your local machine, you must install ruby and jekyll. 
If you want to install jekyll on MacOs, please refer to [link](https://jekyllrb.com/docs/installation/macos/).
Then, move to the root directory of this repository, and type the following to install bundle packages:
```
bundle install
```

To run jekyll, type the following:
```
bundle exec jekyll serve --trace
```

If you encounter an error on webrick, try the below and rerun jekyll:
```
bundle add webrick
```

## Update information
### News
`_data/news.yml` contains information on news of our lab, which will be rendered in `index.md`.

### Members
To edit information on members, see `_data/members.yml`. This data will be rendered by `members.md`.
- `type`: member type in [prof, grad, undergrad]

### Publications
To edit information on publications, see `_data/papers.yml`. This data will by rendered by `publications.md`.

### Photos
To add photos to the gallery, add the image files to `assets/images/photos`. The file format is "YYYY-MM-DD-00.{jpeg,png}". The aspect ratio of each image should be a square (1:1).

## References
* https://tianqi.name/jekyll-TeXt-theme/docs/en/quick-start

