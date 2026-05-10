from . import base_types
from .RestrictedFINXMax140Text import RestrictedFINXMax140Text
from .RestrictedFINXMax350Text import RestrictedFINXMax350Text

class PartyTextInformation4(base_types._BaseFieldType):

	__slots__ = ["_PtyCtctDtls", "_DclrtnDtls"]
	@property
	def PtyCtctDtls(self):
		return self._PtyCtctDtls

	@PtyCtctDtls.setter
	def PtyCtctDtls(self, value):
		self._PtyCtctDtls = value if type(value) != auto else self.make_default("PtyCtctDtls")

	@PtyCtctDtls.deleter
	def PtyCtctDtls(self):
		del self._PtyCtctDtls
		self._PtyCtctDtls = None

	@property
	def DclrtnDtls(self):
		return self._DclrtnDtls

	@DclrtnDtls.setter
	def DclrtnDtls(self, value):
		self._DclrtnDtls = value if type(value) != auto else self.make_default("DclrtnDtls")

	@DclrtnDtls.deleter
	def DclrtnDtls(self):
		del self._DclrtnDtls
		self._DclrtnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PtyCtctDtls', type=RestrictedFINXMax140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DclrtnDtls', type=RestrictedFINXMax350Text, min=0, max=1, mutex_group=None, array=False),
	))

