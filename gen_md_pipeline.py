import json

def gen_json_to_markdown_mermaid(json_path="pd_pipeline.json", target_path="pd_pipeline.md"):
    f = open(json_path)
    data = json.load(f)
    items = data['properties']['activities']

    text_string = """```mermaid
    graph LR;
    classDef copyclass fill:#FFFFFF;
    classDef brickclass fill:#66FFCC;
    """
    for item in items:
        name = item['name']
        depends = [i['activity'] for i in item['dependsOn']]
        conditions = [i['dependencyConditions'] for i in item['dependsOn']]
        
        name = name.replace(" ", "_")

        arrow = "-->||"
        if "copy" in item['type'].lower() or "copy" in name.lower():
            name = name+":::copyclass"
            arrow = ".->||"
        elif "brick" in item['type'].lower():
            name = name+":::brickclass"

        for depend, condition in zip(depends, conditions):
            depend = depend.replace(" ", "_")
            condition = ",".join(condition)
            arrow = arrow.replace("||", "|" + condition + "|")
            text = depend+":::brickclass" + arrow + name+";\n"
            text_string += text

    f = open(target_path, "w")
    f.write(text_string)
    f.close()
#    print(text_string)


gen_json_to_markdown_mermaid(
    "etl01/pipeline/pl_p_tribe_datawarehouse_pd_01.json",
    "graphs/pl_p_tribe_datawarehouse_pd_01.md"
)


gen_json_to_markdown_mermaid(
    "etl01/pipeline/pl_p_tribe_datamart_ad_databrick.json",
    "graphs/pl_p_tribe_datamart_ad_databrick.md"
)


gen_json_to_markdown_mermaid(
    "etl01/pipeline/pl_p_tribe_build_report.json",
    "graphs/pl_p_tribe_build_report.md"
)


gen_json_to_markdown_mermaid(
    "etl01/pipeline/pl_p_tribe_datawarehouse_01.json",
    "graphs/pl_p_tribe_datawarehouse_01.md"
)


gen_json_to_markdown_mermaid(
    "etl01/pipeline/pl_p_tribe_datawarehouse_pd_near_realtime_02.json",
    "graphs/pl_p_tribe_datawarehouse_pd_near_realtime_02.md"
)


gen_json_to_markdown_mermaid(
    "etl01/pipeline/pl_p_tribe_datamart_ad.json",
    "graphs/pl_p_tribe_datamart_ad.md"
)


gen_json_to_markdown_mermaid(
    "etl01/pipeline/pl_p_tribe_datawarehouse_pd_02.json",
    "graphs/pl_p_tribe_datawarehouse_pd_02.md"
)


gen_json_to_markdown_mermaid(
    "jsons/pl_p_tribe_datamart_pd_contest.json",
    "graphs/pl_p_tribe_datamart_pd_contest.md"
)