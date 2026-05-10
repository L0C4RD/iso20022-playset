from . import base_types
from ._SecuritiesAccountActivityAdviceV01 import SecuritiesAccountActivityAdviceV01

class REDA_035_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesAcctActvtyAdvc"]
		@property
		def SctiesAcctActvtyAdvc(self):
			return self._SctiesAcctActvtyAdvc

		@SctiesAcctActvtyAdvc.setter
		def SctiesAcctActvtyAdvc(self, value):
			self._SctiesAcctActvtyAdvc = value if type(value) != base_types.auto else self.make_default("SctiesAcctActvtyAdvc")

		@SctiesAcctActvtyAdvc.deleter
		def SctiesAcctActvtyAdvc(self):
			del self._SctiesAcctActvtyAdvc
			self._SctiesAcctActvtyAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctActvtyAdvc', type=SecuritiesAccountActivityAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

