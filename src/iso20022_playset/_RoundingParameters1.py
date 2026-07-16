# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DecimalNumber
from . import RoundingDirection1Code

class RoundingParameters1(base_types._BaseFieldType):

	__slots__ = ["_RndgDrctn", "_RndgMdlus"]
	@property
	def RndgDrctn(self):
		return self._RndgDrctn

	@RndgDrctn.setter
	def RndgDrctn(self, value):
		self._RndgDrctn = value if value is not None else base_types.UninitialisedField(self, 'RndgDrctn', RoundingDirection1Code, False)

	@RndgDrctn.deleter
	def RndgDrctn(self):
		del self._RndgDrctn
		self._RndgDrctn = base_types.UninitialisedField(self, 'RndgDrctn', RoundingDirection1Code, False)

	@property
	def RndgMdlus(self):
		return self._RndgMdlus

	@RndgMdlus.setter
	def RndgMdlus(self, value):
		self._RndgMdlus = value if value is not None else base_types.UninitialisedField(self, 'RndgMdlus', DecimalNumber, False)

	@RndgMdlus.deleter
	def RndgMdlus(self):
		del self._RndgMdlus
		self._RndgMdlus = base_types.UninitialisedField(self, 'RndgMdlus', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RndgDrctn', type=RoundingDirection1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RndgMdlus', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))