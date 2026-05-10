from . import base_types
from ._Max350Text import Max350Text
from ._Max140Text import Max140Text

class PartyTextInformation5(base_types._BaseFieldType):

	__slots__ = ["_DclrtnDtls", "_PtyCtctDtls"]
	@property
	def DclrtnDtls(self):
		return self._DclrtnDtls

	@DclrtnDtls.setter
	def DclrtnDtls(self, value):
		self._DclrtnDtls = value if type(value) != base_types.auto else self.make_default("DclrtnDtls")

	@DclrtnDtls.deleter
	def DclrtnDtls(self):
		del self._DclrtnDtls
		self._DclrtnDtls = None

	@property
	def PtyCtctDtls(self):
		return self._PtyCtctDtls

	@PtyCtctDtls.setter
	def PtyCtctDtls(self, value):
		self._PtyCtctDtls = value if type(value) != base_types.auto else self.make_default("PtyCtctDtls")

	@PtyCtctDtls.deleter
	def PtyCtctDtls(self):
		del self._PtyCtctDtls
		self._PtyCtctDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DclrtnDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyCtctDtls', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

