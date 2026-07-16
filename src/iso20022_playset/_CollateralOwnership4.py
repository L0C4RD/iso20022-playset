# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification178Choice
from . import YesNoIndicator

class CollateralOwnership4(base_types._BaseFieldType):

	__slots__ = ["_ClntNm", "_Prtry"]
	@property
	def ClntNm(self):
		return self._ClntNm

	@ClntNm.setter
	def ClntNm(self, value):
		self._ClntNm = value if value is not None else base_types.UninitialisedField(self, 'ClntNm', PartyIdentification178Choice, False)

	@ClntNm.deleter
	def ClntNm(self):
		del self._ClntNm
		self._ClntNm = base_types.UninitialisedField(self, 'ClntNm', PartyIdentification178Choice, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', YesNoIndicator, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClntNm', type=PartyIdentification178Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtry', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))