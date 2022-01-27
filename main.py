import xml.etree.ElementTree as ET  # for xml

# 增加换行符 {{{
# https://vae-0118.github.io/2017/11/06/Python%E4%B8%ADXML%E7%9A%84%E8%AF%BB%E5%86%99%E6%80%BB%E7%BB%93/
def __indent(elem, level=0):
    i = "\n" + level*"\t"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "\t"
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            __indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
# }}}

# generate annotations.xml {{{
# https://vae-0118.github.io/2017/11/06/Python%E4%B8%ADXML%E7%9A%84%E8%AF%BB%E5%86%99%E6%80%BB%E7%BB%93/
def gen_annotations_xml(list_of_domain):
    lis = []
    for each in list_of_domain:
        lis.append(each[4:])

    # print(lis)


    root = ET.Element('Annotations')       # 创建根节点
    tree = ET.ElementTree(root)            # 创建文档

    # Annotations 的三个非必要属性
    root.set('start', '0')
    root.set('num', str(len(lis)))
    root.set('total', str(len(lis)))

    for link in lis:
        element = ET.Element('Annotation') # 子节点
        element.set('about', link)         # 这个属性的值可能只是注释
        # element.text = 'default'         # 节点中的文本内容

        Label = ET.SubElement(element, 'Label')
        Label.set('name', '_exclude_')

        AdditionalData = ET.SubElement(element, 'AdditionalData')
        AdditionalData.set('value', link)     # link 地址
        AdditionalData.set('attribute', 'original_url')


        root.append(element)               # 放到根节点下

    __indent(root)          # 增加换行符
    tree.write('annotations.xml', encoding='utf-8', xml_declaration=True)
    ...

# }}}


def main():
    f = open('uBlacklist_subscription.txt', 'r')
    lis = []
    for each in f.readlines():
        lis.append(each.strip())          # 去换行符

    print(lis)

    gen_annotations_xml(lis)

    ...


if __name__ == '__main__':

    main()

