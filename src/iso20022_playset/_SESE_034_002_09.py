from . import base_types
from ._SecuritiesFinancingStatusAdvice002V09 import SecuritiesFinancingStatusAdvice002V09

class SESE_034_002_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesFincgStsAdvc"]
		@property
		def SctiesFincgStsAdvc(self):
			return self._SctiesFincgStsAdvc

		@SctiesFincgStsAdvc.setter
		def SctiesFincgStsAdvc(self, value):
			self._SctiesFincgStsAdvc = value if type(value) != base_types.auto else self.make_default("SctiesFincgStsAdvc")

		@SctiesFincgStsAdvc.deleter
		def SctiesFincgStsAdvc(self):
			del self._SctiesFincgStsAdvc
			self._SctiesFincgStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgStsAdvc', type=SecuritiesFinancingStatusAdvice002V09, min=1, max=1, mutex_group=None, array=False),
		))

