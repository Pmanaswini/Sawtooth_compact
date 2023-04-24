// This file is generated by rust-protobuf 2.28.0. Do not edit
// @generated

// https://github.com/rust-lang/rust-clippy/issues/702
#![allow(unknown_lints)]
#![allow(clippy::all)]

#![allow(unused_attributes)]
#![cfg_attr(rustfmt, rustfmt::skip)]

#![allow(box_pointers)]
#![allow(dead_code)]
#![allow(missing_docs)]
#![allow(non_camel_case_types)]
#![allow(non_snake_case)]
#![allow(non_upper_case_globals)]
#![allow(trivial_casts)]
#![allow(unused_imports)]
#![allow(unused_results)]
//! Generated file from `client_receipt.proto`

/// Generated files are compatible only with the same version
/// of protobuf runtime.
// const _PROTOBUF_VERSION_CHECK: () = ::protobuf::VERSION_2_28_0;

#[derive(PartialEq,Clone,Default)]
pub struct ClientReceiptGetRequest {
    // message fields
    pub transaction_ids: ::protobuf::RepeatedField<::std::string::String>,
    // special fields
    pub unknown_fields: ::protobuf::UnknownFields,
    pub cached_size: ::protobuf::CachedSize,
}

impl<'a> ::std::default::Default for &'a ClientReceiptGetRequest {
    fn default() -> &'a ClientReceiptGetRequest {
        <ClientReceiptGetRequest as ::protobuf::Message>::default_instance()
    }
}

impl ClientReceiptGetRequest {
    pub fn new() -> ClientReceiptGetRequest {
        ::std::default::Default::default()
    }

    // repeated string transaction_ids = 1;


    pub fn get_transaction_ids(&self) -> &[::std::string::String] {
        &self.transaction_ids
    }
    pub fn clear_transaction_ids(&mut self) {
        self.transaction_ids.clear();
    }

    // Param is passed by value, moved
    pub fn set_transaction_ids(&mut self, v: ::protobuf::RepeatedField<::std::string::String>) {
        self.transaction_ids = v;
    }

    // Mutable pointer to the field.
    pub fn mut_transaction_ids(&mut self) -> &mut ::protobuf::RepeatedField<::std::string::String> {
        &mut self.transaction_ids
    }

    // Take field
    pub fn take_transaction_ids(&mut self) -> ::protobuf::RepeatedField<::std::string::String> {
        ::std::mem::replace(&mut self.transaction_ids, ::protobuf::RepeatedField::new())
    }
}

impl ::protobuf::Message for ClientReceiptGetRequest {
    fn is_initialized(&self) -> bool {
        true
    }

    fn merge_from(&mut self, is: &mut ::protobuf::CodedInputStream<'_>) -> ::protobuf::ProtobufResult<()> {
        while !is.eof()? {
            let (field_number, wire_type) = is.read_tag_unpack()?;
            match field_number {
                1 => {
                    ::protobuf::rt::read_repeated_string_into(wire_type, is, &mut self.transaction_ids)?;
                },
                _ => {
                    ::protobuf::rt::read_unknown_or_skip_group(field_number, wire_type, is, self.mut_unknown_fields())?;
                },
            };
        }
        ::std::result::Result::Ok(())
    }

    // Compute sizes of nested messages
    #[allow(unused_variables)]
    fn compute_size(&self) -> u32 {
        let mut my_size = 0;
        for value in &self.transaction_ids {
            my_size += ::protobuf::rt::string_size(1, &value);
        };
        my_size += ::protobuf::rt::unknown_fields_size(self.get_unknown_fields());
        self.cached_size.set(my_size);
        my_size
    }

    fn write_to_with_cached_sizes(&self, os: &mut ::protobuf::CodedOutputStream<'_>) -> ::protobuf::ProtobufResult<()> {
        for v in &self.transaction_ids {
            os.write_string(1, &v)?;
        };
        os.write_unknown_fields(self.get_unknown_fields())?;
        ::std::result::Result::Ok(())
    }

    fn get_cached_size(&self) -> u32 {
        self.cached_size.get()
    }

    fn get_unknown_fields(&self) -> &::protobuf::UnknownFields {
        &self.unknown_fields
    }

    fn mut_unknown_fields(&mut self) -> &mut ::protobuf::UnknownFields {
        &mut self.unknown_fields
    }

    fn as_any(&self) -> &dyn (::std::any::Any) {
        self as &dyn (::std::any::Any)
    }
    fn as_any_mut(&mut self) -> &mut dyn (::std::any::Any) {
        self as &mut dyn (::std::any::Any)
    }
    fn into_any(self: ::std::boxed::Box<Self>) -> ::std::boxed::Box<dyn (::std::any::Any)> {
        self
    }

    fn descriptor(&self) -> &'static ::protobuf::reflect::MessageDescriptor {
        Self::descriptor_static()
    }

    fn new() -> ClientReceiptGetRequest {
        ClientReceiptGetRequest::new()
    }

    fn descriptor_static() -> &'static ::protobuf::reflect::MessageDescriptor {
        static descriptor: ::protobuf::rt::LazyV2<::protobuf::reflect::MessageDescriptor> = ::protobuf::rt::LazyV2::INIT;
        descriptor.get(|| {
            let mut fields = ::std::vec::Vec::new();
            fields.push(::protobuf::reflect::accessor::make_repeated_field_accessor::<_, ::protobuf::types::ProtobufTypeString>(
                "transaction_ids",
                |m: &ClientReceiptGetRequest| { &m.transaction_ids },
                |m: &mut ClientReceiptGetRequest| { &mut m.transaction_ids },
            ));
            ::protobuf::reflect::MessageDescriptor::new_pb_name::<ClientReceiptGetRequest>(
                "ClientReceiptGetRequest",
                fields,
                file_descriptor_proto()
            )
        })
    }

    fn default_instance() -> &'static ClientReceiptGetRequest {
        static instance: ::protobuf::rt::LazyV2<ClientReceiptGetRequest> = ::protobuf::rt::LazyV2::INIT;
        instance.get(ClientReceiptGetRequest::new)
    }
}

impl ::protobuf::Clear for ClientReceiptGetRequest {
    fn clear(&mut self) {
        self.transaction_ids.clear();
        self.unknown_fields.clear();
    }
}

impl ::std::fmt::Debug for ClientReceiptGetRequest {
    fn fmt(&self, f: &mut ::std::fmt::Formatter<'_>) -> ::std::fmt::Result {
        ::protobuf::text_format::fmt(self, f)
    }
}

impl ::protobuf::reflect::ProtobufValue for ClientReceiptGetRequest {
    fn as_ref(&self) -> ::protobuf::reflect::ReflectValueRef {
        ::protobuf::reflect::ReflectValueRef::Message(self)
    }
}

#[derive(PartialEq,Clone,Default)]
pub struct ClientReceiptGetResponse {
    // message fields
    pub status: ClientReceiptGetResponse_Status,
    pub receipts: ::protobuf::RepeatedField<super::transaction_receipt::TransactionReceipt>,
    // special fields
    pub unknown_fields: ::protobuf::UnknownFields,
    pub cached_size: ::protobuf::CachedSize,
}

impl<'a> ::std::default::Default for &'a ClientReceiptGetResponse {
    fn default() -> &'a ClientReceiptGetResponse {
        <ClientReceiptGetResponse as ::protobuf::Message>::default_instance()
    }
}

impl ClientReceiptGetResponse {
    pub fn new() -> ClientReceiptGetResponse {
        ::std::default::Default::default()
    }

    // .ClientReceiptGetResponse.Status status = 1;


    pub fn get_status(&self) -> ClientReceiptGetResponse_Status {
        self.status
    }
    pub fn clear_status(&mut self) {
        self.status = ClientReceiptGetResponse_Status::STATUS_UNSET;
    }

    // Param is passed by value, moved
    pub fn set_status(&mut self, v: ClientReceiptGetResponse_Status) {
        self.status = v;
    }

    // repeated .TransactionReceipt receipts = 2;


    pub fn get_receipts(&self) -> &[super::transaction_receipt::TransactionReceipt] {
        &self.receipts
    }
    pub fn clear_receipts(&mut self) {
        self.receipts.clear();
    }

    // Param is passed by value, moved
    pub fn set_receipts(&mut self, v: ::protobuf::RepeatedField<super::transaction_receipt::TransactionReceipt>) {
        self.receipts = v;
    }

    // Mutable pointer to the field.
    pub fn mut_receipts(&mut self) -> &mut ::protobuf::RepeatedField<super::transaction_receipt::TransactionReceipt> {
        &mut self.receipts
    }

    // Take field
    pub fn take_receipts(&mut self) -> ::protobuf::RepeatedField<super::transaction_receipt::TransactionReceipt> {
        ::std::mem::replace(&mut self.receipts, ::protobuf::RepeatedField::new())
    }
}

impl ::protobuf::Message for ClientReceiptGetResponse {
    fn is_initialized(&self) -> bool {
        for v in &self.receipts {
            if !v.is_initialized() {
                return false;
            }
        };
        true
    }

    fn merge_from(&mut self, is: &mut ::protobuf::CodedInputStream<'_>) -> ::protobuf::ProtobufResult<()> {
        while !is.eof()? {
            let (field_number, wire_type) = is.read_tag_unpack()?;
            match field_number {
                1 => {
                    ::protobuf::rt::read_proto3_enum_with_unknown_fields_into(wire_type, is, &mut self.status, 1, &mut self.unknown_fields)?
                },
                2 => {
                    ::protobuf::rt::read_repeated_message_into(wire_type, is, &mut self.receipts)?;
                },
                _ => {
                    ::protobuf::rt::read_unknown_or_skip_group(field_number, wire_type, is, self.mut_unknown_fields())?;
                },
            };
        }
        ::std::result::Result::Ok(())
    }

    // Compute sizes of nested messages
    #[allow(unused_variables)]
    fn compute_size(&self) -> u32 {
        let mut my_size = 0;
        if self.status != ClientReceiptGetResponse_Status::STATUS_UNSET {
            my_size += ::protobuf::rt::enum_size(1, self.status);
        }
        for value in &self.receipts {
            let len = value.compute_size();
            my_size += 1 + ::protobuf::rt::compute_raw_varint32_size(len) + len;
        };
        my_size += ::protobuf::rt::unknown_fields_size(self.get_unknown_fields());
        self.cached_size.set(my_size);
        my_size
    }

    fn write_to_with_cached_sizes(&self, os: &mut ::protobuf::CodedOutputStream<'_>) -> ::protobuf::ProtobufResult<()> {
        if self.status != ClientReceiptGetResponse_Status::STATUS_UNSET {
            os.write_enum(1, ::protobuf::ProtobufEnum::value(&self.status))?;
        }
        for v in &self.receipts {
            os.write_tag(2, ::protobuf::wire_format::WireTypeLengthDelimited)?;
            os.write_raw_varint32(v.get_cached_size())?;
            v.write_to_with_cached_sizes(os)?;
        };
        os.write_unknown_fields(self.get_unknown_fields())?;
        ::std::result::Result::Ok(())
    }

    fn get_cached_size(&self) -> u32 {
        self.cached_size.get()
    }

    fn get_unknown_fields(&self) -> &::protobuf::UnknownFields {
        &self.unknown_fields
    }

    fn mut_unknown_fields(&mut self) -> &mut ::protobuf::UnknownFields {
        &mut self.unknown_fields
    }

    fn as_any(&self) -> &dyn (::std::any::Any) {
        self as &dyn (::std::any::Any)
    }
    fn as_any_mut(&mut self) -> &mut dyn (::std::any::Any) {
        self as &mut dyn (::std::any::Any)
    }
    fn into_any(self: ::std::boxed::Box<Self>) -> ::std::boxed::Box<dyn (::std::any::Any)> {
        self
    }

    fn descriptor(&self) -> &'static ::protobuf::reflect::MessageDescriptor {
        Self::descriptor_static()
    }

    fn new() -> ClientReceiptGetResponse {
        ClientReceiptGetResponse::new()
    }

    fn descriptor_static() -> &'static ::protobuf::reflect::MessageDescriptor {
        static descriptor: ::protobuf::rt::LazyV2<::protobuf::reflect::MessageDescriptor> = ::protobuf::rt::LazyV2::INIT;
        descriptor.get(|| {
            let mut fields = ::std::vec::Vec::new();
            fields.push(::protobuf::reflect::accessor::make_simple_field_accessor::<_, ::protobuf::types::ProtobufTypeEnum<ClientReceiptGetResponse_Status>>(
                "status",
                |m: &ClientReceiptGetResponse| { &m.status },
                |m: &mut ClientReceiptGetResponse| { &mut m.status },
            ));
            fields.push(::protobuf::reflect::accessor::make_repeated_field_accessor::<_, ::protobuf::types::ProtobufTypeMessage<super::transaction_receipt::TransactionReceipt>>(
                "receipts",
                |m: &ClientReceiptGetResponse| { &m.receipts },
                |m: &mut ClientReceiptGetResponse| { &mut m.receipts },
            ));
            ::protobuf::reflect::MessageDescriptor::new_pb_name::<ClientReceiptGetResponse>(
                "ClientReceiptGetResponse",
                fields,
                file_descriptor_proto()
            )
        })
    }

    fn default_instance() -> &'static ClientReceiptGetResponse {
        static instance: ::protobuf::rt::LazyV2<ClientReceiptGetResponse> = ::protobuf::rt::LazyV2::INIT;
        instance.get(ClientReceiptGetResponse::new)
    }
}

impl ::protobuf::Clear for ClientReceiptGetResponse {
    fn clear(&mut self) {
        self.status = ClientReceiptGetResponse_Status::STATUS_UNSET;
        self.receipts.clear();
        self.unknown_fields.clear();
    }
}

impl ::std::fmt::Debug for ClientReceiptGetResponse {
    fn fmt(&self, f: &mut ::std::fmt::Formatter<'_>) -> ::std::fmt::Result {
        ::protobuf::text_format::fmt(self, f)
    }
}

impl ::protobuf::reflect::ProtobufValue for ClientReceiptGetResponse {
    fn as_ref(&self) -> ::protobuf::reflect::ReflectValueRef {
        ::protobuf::reflect::ReflectValueRef::Message(self)
    }
}

#[derive(Clone,PartialEq,Eq,Debug,Hash)]
pub enum ClientReceiptGetResponse_Status {
    STATUS_UNSET = 0,
    OK = 1,
    INTERNAL_ERROR = 2,
    NO_RESOURCE = 5,
    INVALID_ID = 8,
}

impl ::protobuf::ProtobufEnum for ClientReceiptGetResponse_Status {
    fn value(&self) -> i32 {
        *self as i32
    }

    fn from_i32(value: i32) -> ::std::option::Option<ClientReceiptGetResponse_Status> {
        match value {
            0 => ::std::option::Option::Some(ClientReceiptGetResponse_Status::STATUS_UNSET),
            1 => ::std::option::Option::Some(ClientReceiptGetResponse_Status::OK),
            2 => ::std::option::Option::Some(ClientReceiptGetResponse_Status::INTERNAL_ERROR),
            5 => ::std::option::Option::Some(ClientReceiptGetResponse_Status::NO_RESOURCE),
            8 => ::std::option::Option::Some(ClientReceiptGetResponse_Status::INVALID_ID),
            _ => ::std::option::Option::None
        }
    }

    fn values() -> &'static [Self] {
        static values: &'static [ClientReceiptGetResponse_Status] = &[
            ClientReceiptGetResponse_Status::STATUS_UNSET,
            ClientReceiptGetResponse_Status::OK,
            ClientReceiptGetResponse_Status::INTERNAL_ERROR,
            ClientReceiptGetResponse_Status::NO_RESOURCE,
            ClientReceiptGetResponse_Status::INVALID_ID,
        ];
        values
    }

    fn enum_descriptor_static() -> &'static ::protobuf::reflect::EnumDescriptor {
        static descriptor: ::protobuf::rt::LazyV2<::protobuf::reflect::EnumDescriptor> = ::protobuf::rt::LazyV2::INIT;
        descriptor.get(|| {
            ::protobuf::reflect::EnumDescriptor::new_pb_name::<ClientReceiptGetResponse_Status>("ClientReceiptGetResponse.Status", file_descriptor_proto())
        })
    }
}

impl ::std::marker::Copy for ClientReceiptGetResponse_Status {
}

impl ::std::default::Default for ClientReceiptGetResponse_Status {
    fn default() -> Self {
        ClientReceiptGetResponse_Status::STATUS_UNSET
    }
}

impl ::protobuf::reflect::ProtobufValue for ClientReceiptGetResponse_Status {
    fn as_ref(&self) -> ::protobuf::reflect::ReflectValueRef {
        ::protobuf::reflect::ReflectValueRef::Enum(::protobuf::ProtobufEnum::descriptor(self))
    }
}

static file_descriptor_proto_data: &'static [u8] = b"\
    \n\x14client_receipt.proto\x1a\x19transaction_receipt.proto\"B\n\x17Clie\
    ntReceiptGetRequest\x12'\n\x0ftransaction_ids\x18\x01\x20\x03(\tR\x0etra\
    nsactionIds\"\xde\x01\n\x18ClientReceiptGetResponse\x128\n\x06status\x18\
    \x01\x20\x01(\x0e2\x20.ClientReceiptGetResponse.StatusR\x06status\x12/\n\
    \x08receipts\x18\x02\x20\x03(\x0b2\x13.TransactionReceiptR\x08receipts\"\
    W\n\x06Status\x12\x10\n\x0cSTATUS_UNSET\x10\0\x12\x06\n\x02OK\x10\x01\
    \x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\x0f\n\x0bNO_RESOURCE\x10\x05\
    \x12\x0e\n\nINVALID_ID\x10\x08B-\n\x15sawtooth.sdk.protobufP\x01Z\x12cli\
    ent_receipt_pb2b\x06proto3\
";

static file_descriptor_proto_lazy: ::protobuf::rt::LazyV2<::protobuf::descriptor::FileDescriptorProto> = ::protobuf::rt::LazyV2::INIT;

fn parse_descriptor_proto() -> ::protobuf::descriptor::FileDescriptorProto {
    ::protobuf::Message::parse_from_bytes(file_descriptor_proto_data).unwrap()
}

pub fn file_descriptor_proto() -> &'static ::protobuf::descriptor::FileDescriptorProto {
    file_descriptor_proto_lazy.get(|| {
        parse_descriptor_proto()
    })
}