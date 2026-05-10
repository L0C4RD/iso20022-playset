import base_types
import ShareholderIdentificationDisclosureResponseStatusAdviceV01

class SEEV_049_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ShrhldrIdDsclsrRspnStsAdvc"]
		@property
		def ShrhldrIdDsclsrRspnStsAdvc(self):
			return self._ShrhldrIdDsclsrRspnStsAdvc

		@ShrhldrIdDsclsrRspnStsAdvc.setter
		def ShrhldrIdDsclsrRspnStsAdvc(self, value):
			self._ShrhldrIdDsclsrRspnStsAdvc = value if type(value) != auto else self.make_default("ShrhldrIdDsclsrRspnStsAdvc")

		@ShrhldrIdDsclsrRspnStsAdvc.deleter
		def ShrhldrIdDsclsrRspnStsAdvc(self):
			del self._ShrhldrIdDsclsrRspnStsAdvc
			self._ShrhldrIdDsclsrRspnStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ShrhldrIdDsclsrRspnStsAdvc', type=ShareholderIdentificationDisclosureResponseStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

