from . import base_types
from .AccountLinkStatusAdviceV01 import AccountLinkStatusAdviceV01

class REDA_051_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctLkStsAdvc"]
		@property
		def AcctLkStsAdvc(self):
			return self._AcctLkStsAdvc

		@AcctLkStsAdvc.setter
		def AcctLkStsAdvc(self, value):
			self._AcctLkStsAdvc = value if type(value) != auto else self.make_default("AcctLkStsAdvc")

		@AcctLkStsAdvc.deleter
		def AcctLkStsAdvc(self):
			del self._AcctLkStsAdvc
			self._AcctLkStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctLkStsAdvc', type=AccountLinkStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))

