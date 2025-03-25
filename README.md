# water-sample-schema

Sample LinkML project setup for 2024 paper figures

## Website

[https://sierra-moxon.github.io/water-sample-schema](https://sierra-moxon.github.io/water-sample-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [environmental_sample_schema](src/environmental_sample_schema)
    * [schema](src/environmental_sample_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/environmental_sample_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
