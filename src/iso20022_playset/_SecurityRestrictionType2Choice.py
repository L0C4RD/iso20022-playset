# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification30
from . import RestrictionType1Code

class SecurityRestrictionType2Choice(base_types._BaseFieldType):

	__slots__ = ["_PrtryRstrctn", "_RstrctnTp"]
	@property
	def PrtryRstrctn(self):
		return self._PrtryRstrctn

	@PrtryRstrctn.setter
	def PrtryRstrctn(self, value):
		self._PrtryRstrctn = value if value is not None else base_types.UninitialisedField(self, 'PrtryRstrctn', GenericIdentification30, False)

	@PrtryRstrctn.deleter
	def PrtryRstrctn(self):
		del self._PrtryRstrctn
		self._PrtryRstrctn = base_types.UninitialisedField(self, 'PrtryRstrctn', GenericIdentification30, False)

	@property
	def RstrctnTp(self):
		return self._RstrctnTp

	@RstrctnTp.setter
	def RstrctnTp(self, value):
		self._RstrctnTp = value if value is not None else base_types.UninitialisedField(self, 'RstrctnTp', RestrictionType1Code, False)

	@RstrctnTp.deleter
	def RstrctnTp(self):
		del self._RstrctnTp
		self._RstrctnTp = base_types.UninitialisedField(self, 'RstrctnTp', RestrictionType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtryRstrctn', type=GenericIdentification30, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RstrctnTp', type=RestrictionType1Code, min=0, max=1, mutex_group=1, array=False),
	))