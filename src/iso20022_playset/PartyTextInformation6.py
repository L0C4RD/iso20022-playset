import base_types
import PostalAddress1
import Max350Text
import Max140Text

class PartyTextInformation6(base_types._BaseFieldType):

	__slots__ = ["_RegnAdr", "_PtyCtctDtls", "_DclrtnDtls", "_RegnDtls"]
	@property
	def RegnAdr(self):
		return self._RegnAdr

	@RegnAdr.setter
	def RegnAdr(self, value):
		self._RegnAdr = value if type(value) != auto else self.make_default("RegnAdr")

	@RegnAdr.deleter
	def RegnAdr(self):
		del self._RegnAdr
		self._RegnAdr = None

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
		base_types.FieldEntry(name='RegnAdr', type=PostalAddress1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyCtctDtls', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DclrtnDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))

