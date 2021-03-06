# source: http://www.usb.org/developers/docs/devclass_docs/CDC1.2_WMC1.1_012011.zip, 2017-01-08


class SUBCLASS:
    DIRECT_LINE_CONTROL_MODEL = 0x01
    ABSTRACT_CONTROL_MODEL = 0x02
    TELEPHONE_CONTROL_MODEL = 0x03
    MUTLI_CHANNEL_CONTROL_MODEL = 0x04
    CAPI_CONTROL_MODEL = 0x05
    ETHERNET_NETWORKING_CONTROL_MODEL = 0x06
    ATM_NETWORKING_CONTROL_MODEL = 0x07
    WIRELESS_HANDSET_CONTROL_MODEL = 0x08
    DEVICE_MANAGEMENT = 0x09
    MOBILE_DIRECT_LINE_MODEL = 0x0A
    OBEX = 0x0B
    ETHERNET_EMULATION_MODEL = 0x0C
    NETWORK_CONTROL_MODEL = 0x0D


class PROTOCOL:
    NO_CLASS_SPECIFIC_PROTOCOL = 0x00
    AT_COMMANDS_V250 = 0x01
    AT_COMMANDS_PCCA101 = 0x02
    AT_COMMANDS_PCCA101_ANNEXO = 0x03
    AT_COMMANDS_GSM0707 = 0x04
    AT_COMMANDS_3GPP27007 = 0x05
    AT_COMMANDS_TIA_CDMA = 0x06
    ETHERNET_EMULATION_MODEL = 0x07
    EXTERNAL_PROTOCOL = 0xFE
    VENDOR_SPECIFIC = 0xFF


class DATA_PROTOCOL:
    NO_CLASS_SPECIFIC_PROTOCOL = 0x00
    NETWORK_TRANSFER_BLOCK = 0x01
    ISDN_BRI = 0x30
    HDLC = 0x31
    TRANSPARENT = 0x32
    MANAGEMENT_PROTOCOL_Q921 = 0x50
    DATA_LINK_PROTOCOL_Q931 = 0x51
    TEI_MULTIPLEXOR_Q921 = 0x52
    DATA_COMPRESSION_PROCEDURES = 0x90
    EURO_ISDN_PROTOCOL_CONTROL = 0x91
    V24_RATE_ADAPTION_TO_ISDN = 0x92
    CAPI_COMMANDS = 0x93
    HOST_BASED_DRIVER = 0xFD
    EXTERNAL_PROTOCOL = 0xFE
    VENDOR_SPECIFIC = 0xFF


class DESCRIPTOR_SUBTYPE:
    HEADER_FUNCTIONAL_DESCRIPTOR = 0x00
    CALL_MANAGEMENT_FUNCTIONAL_DESCRIPTOR = 0x01
    ABSTRACT_CONTROL_MANAGEMENT_FUNCTIONAL_DESCRIPTOR = 0x02
    DIRECT_LINE_MANAGEMENT_FUNCTIONAL_DESCRIPTOR = 0x03
    TELEPHONE_RINGER_FUNCTIONAL_DESCRIPTOR = 0x04
    TELEPHONE_CALL_AND_LINE_STATE_REPORTING_CAPABILITIES_FUNCTIONAL_DESCRIPTOR = 0x05
    UNION_FUNCTIONAL_DESCRIPTOR = 0x06
    COUNTRY_SELECTION_FUNCTIONAL_DESCRIPTOR = 0x07
    TELEPHONE_OPERATIONAL_MODES_FUNCTIONAL_DESCRIPTOR = 0x08
    USB_TERMINAL_FUNCTIONAL_DESCRIPTOR = 0x09
    NETWORK_CHANNEL_TERMINAL_DESCRIPTOR = 0x0A
    PROTOCOL_UNIT_FUNCTIONAL_DESCRIPTOR = 0x0B
    EXTENSION_UNIT_FUNCTIONAL_DESCRIPTOR = 0x0C
    MULTI_CHANNEL_MANAGEMENT_FUNCTIONAL_DESCRIPTOR = 0x0D
    CAPI_CONTROL_MANAGEMENT_FUNCTIONAL_DESCRIPTOR = 0x0E
    ETHERNET_NETWORKING_FUNCTIONAL_DESCRIPTOR = 0x0F
    ATM_NETWORKING_FUNCTIONAL_DESCRIPTOR = 0x10
    WIRELESS_HANDSET_CONTROL_MODEL_FUNCTIONAL_DESCRIPTOR = 0x11
    MOBILE_DIRECT_LINE_MODEL_FUNCTIONAL_DESCRIPTOR = 0x12
    MDLM_DETAIL_FUNCTIONAL_DESCRIPTOR = 0x13
    DEVICE_MANAGEMENT_MODEL_FUNCTIONAL_DESCRIPTOR = 0x14
    OBEX_FUNCTIONAL_DESCRIPTOR = 0x15
    COMMAND_SET_FUNCTIONAL_DESCRIPTOR = 0x16
    COMMAND_SET_DETAIL_FUNCTIONAL_DESCRIPTOR = 0x17
    TELEPHONE_CONTROL_MODEL_FUNCTIONAL_DESCRIPTOR = 0x18
    OBEX_SERVICE_IDENTIFIER_FUNCTIONAL_DESCRIPTOR = 0x19
    NCM_FUNCTIONAL_DESCRIPTOR = 0x1A
