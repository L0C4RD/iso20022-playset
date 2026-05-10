import base_types
import SecuritiesMessageCancellationAdvice002V07

class SEMT_020_002_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesMsgCxlAdvc"]
		@property
		def SctiesMsgCxlAdvc(self):
			return self._SctiesMsgCxlAdvc

		@SctiesMsgCxlAdvc.setter
		def SctiesMsgCxlAdvc(self, value):
			self._SctiesMsgCxlAdvc = value if type(value) != auto else self.make_default("SctiesMsgCxlAdvc")

		@SctiesMsgCxlAdvc.deleter
		def SctiesMsgCxlAdvc(self):
			del self._SctiesMsgCxlAdvc
			self._SctiesMsgCxlAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesMsgCxlAdvc', type=SecuritiesMessageCancellationAdvice002V07, min=1, max=1, mutex_group=None, array=False),
		))

