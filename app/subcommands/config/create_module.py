from app.helper import prints
from app.schemas.modules import Module,Submodule
from app.core.config import settings

def create(module: Module):
    path = f"{settings.BASE_PATH}/{settings.MODULE_PATH}/{module.semester}_{module.name}.md"
    sub_paths = create_submodules(module_identifier=module.identifier, path=path, submodules=module.submodules,module_name=module.name,module_semester=module.semester)

    with open(path,"w",encoding="utf-8") as f:
        f.write("---\n")
        f.write(f"Identifier: {module.identifier}\n")
        f.write(f"Name: {module.name}\n")
        f.write(f"Semester: {module.semester}\n")
        f.write(f"submodules_identifier:\n")
        for submodule in module.submodules:
            f.write(f"  - {submodule.identifier}\n")
        f.write("submodules_links:\n")
        for submodule in sub_paths:
            f.write(f"  - [[{submodule}]]\n")

        if module.exam_format:
            f.write(f"ExamFormat: {module.exam_format}\n")
        f.write("---\n")

        f.write(f"# {module.name}\n")
        f.write("## Beschreibung\n")


def create_submodules(module_identifier:str,module_name:str,module_semester:str,path: str, submodules: list[Submodule]):
    tmp_paths = []

    for submodule in submodules:
        tmp_path = f"{settings.SUBMODULES_PATH}/{module_semester}_{str(submodule.order).zfill(2)}_{module_name}_{submodule.name}.md"
        tmp_paths.append(tmp_path)
        with open(f"{settings.BASE_PATH}/{tmp_path}","w",encoding="utf-8") as f:
            f.write("---\n")
            f.write(f"Identifier: {submodule.identifier}\n")
            f.write(f"Name: {submodule.name}\n")
            f.write(f"Order: {submodule.order}\n")
            f.write(f"ModuleIdentifier: {module_identifier}\n")
            f.write(f"Module: [[{path.split(settings.BASE_PATH)[-1]}]]\n")
            f.write("---\n")

            f.write(f"# {submodule.name}\n")
            f.write("## Beschreibung\n")

    return tmp_paths