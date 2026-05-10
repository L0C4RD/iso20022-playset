from . import base_types
from .SecuritiesFinancingStatusAdviceV10 import SecuritiesFinancingStatusAdviceV10

class SESE_034_001_10():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesFincgStsAdvc"]
		@property
		def SctiesFincgStsAdvc(self):
			return self._SctiesFincgStsAdvc

		@SctiesFincgStsAdvc.setter
		def SctiesFincgStsAdvc(self, value):
			self._SctiesFincgStsAdvc = value if type(value) != auto else self.make_default("SctiesFincgStsAdvc")

		@SctiesFincgStsAdvc.deleter
		def SctiesFincgStsAdvc(self):
			del self._SctiesFincgStsAdvc
			self._SctiesFincgStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgStsAdvc', type=SecuritiesFinancingStatusAdviceV10, min=1, max=1, mutex_group=None, array=False),
		))

