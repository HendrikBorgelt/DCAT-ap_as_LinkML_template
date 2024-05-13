# DCATlinkML

A LinkML representation of DCAT-AP is being developed in this repository. This is intended to achieve several goals:

 - Through LinkML modeling, other file formats such as JSON, YAML, CSV, etc. can be checked against a simple LinkML profile and then converted into an RDF representation. This makes it easier for developers who do not want to work in RDF formats, but at the same time makes it possible to create simpler pipelines, as the RDF representation can be generated automatically using LinkML.
- Since JSON and YAML are broader formats than SHACL, the modeling of DCAT-AP using LinkML is intended to make the structures more readable and easier to interpret. This in turn simplifies programming for developers, as no new syntax in the form of SHACL needs to be learned.
- In order to modify and adapt DCAT-AP, extensions must currently be written natively in SHACL, as no other formats are offered. This is difficult even for many semanticists who are familiar with SHACL, as there are only a few programs that support this. Programming with LinkML offers the advantage that syntax errors can be detected using the Python tools of the LinkML community, which makes programming easier.

While a LinkML representation is offered here, it does not offer all the structures that are also offered by DCAT-AP and, in case of doubt, cannot represent them in the same way. This is partly due to the structures provided by LinkML, and partly because some of these structures have simply not yet been developed. We hope for active support from all those who want to support this project.

## Website

The current LinkML meatdata model of DCAT-AP kann be found here:
[https://hendrikborgelt.github.io/DCATlinkML](https://hendrikborgelt.github.io/DCAT-ap_as_LinkML_template/)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [dcatlinkml](src/dcatlinkml)
    * [schema](src/dcatlinkml/schema) -- LinkML schema
      (edit this)

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
