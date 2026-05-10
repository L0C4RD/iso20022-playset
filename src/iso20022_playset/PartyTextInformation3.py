from . import base_types
import RestrictedFINXMax350Text
import RestrictedFINXMax140Text

class PartyTextInformation3(base_types._BaseFieldType):

	__slots__ = ["_DclrtnDtls", "_PtyCtctDtls", "_RegnDtls"]
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
	def RegnDtls(self):
		return self._RegnDtls

	@RegnDtls.setter
	def RegnDtls(self, value):
		self._RegnDtls = value if type(value) != auto else self.make_default("RegnDtls")

	@RegnDtls.deleter
	def RegnDtls(self):
		del self._RegnDtls
		self._RegnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DclrtnDtls', type=RestrictedFINXMax350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyCtctDtls', type=RestrictedFINXMax140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnDtls', type=RestrictedFINXMax350Text, min=0, max=1, mutex_group=None, array=False),
	))

