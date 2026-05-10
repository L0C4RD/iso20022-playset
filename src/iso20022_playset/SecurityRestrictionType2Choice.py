import base_types
import GenericIdentification30
import RestrictionType1Code

class SecurityRestrictionType2Choice(base_types._BaseFieldType):

	__slots__ = ["_RstrctnTp", "_PrtryRstrctn"]
	@property
	def RstrctnTp(self):
		return self._RstrctnTp

	@RstrctnTp.setter
	def RstrctnTp(self, value):
		self._RstrctnTp = value if type(value) != auto else self.make_default("RstrctnTp")

	@RstrctnTp.deleter
	def RstrctnTp(self):
		del self._RstrctnTp
		self._RstrctnTp = None

	@property
	def PrtryRstrctn(self):
		return self._PrtryRstrctn

	@PrtryRstrctn.setter
	def PrtryRstrctn(self, value):
		self._PrtryRstrctn = value if type(value) != auto else self.make_default("PrtryRstrctn")

	@PrtryRstrctn.deleter
	def PrtryRstrctn(self):
		del self._PrtryRstrctn
		self._PrtryRstrctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RstrctnTp', type=RestrictionType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryRstrctn', type=GenericIdentification30, min=0, max=1, mutex_group=1, array=False),
	))

