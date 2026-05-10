from . import base_types
import ShareholderIdentificationDisclosureResponseCancellationAdviceV01

class SEEV_048_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ShrhldrIdDsclsrRspnCxlAdvc"]
		@property
		def ShrhldrIdDsclsrRspnCxlAdvc(self):
			return self._ShrhldrIdDsclsrRspnCxlAdvc

		@ShrhldrIdDsclsrRspnCxlAdvc.setter
		def ShrhldrIdDsclsrRspnCxlAdvc(self, value):
			self._ShrhldrIdDsclsrRspnCxlAdvc = value if type(value) != auto else self.make_default("ShrhldrIdDsclsrRspnCxlAdvc")

		@ShrhldrIdDsclsrRspnCxlAdvc.deleter
		def ShrhldrIdDsclsrRspnCxlAdvc(self):
			del self._ShrhldrIdDsclsrRspnCxlAdvc
			self._ShrhldrIdDsclsrRspnCxlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ShrhldrIdDsclsrRspnCxlAdvc', type=ShareholderIdentificationDisclosureResponseCancellationAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

