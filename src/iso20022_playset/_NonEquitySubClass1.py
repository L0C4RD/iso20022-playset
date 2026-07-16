# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max1000Text
from . import NonEquitySubClassSegmentationCriterion1

class NonEquitySubClass1(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_SgmttnCrit"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max1000Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max1000Text, False)

	@property
	def SgmttnCrit(self):
		return self._SgmttnCrit

	@SgmttnCrit.setter
	def SgmttnCrit(self, value):
		self._SgmttnCrit = value if value is not None else base_types.UninitialisedField(self, 'SgmttnCrit', NonEquitySubClassSegmentationCriterion1, True)

	@SgmttnCrit.deleter
	def SgmttnCrit(self):
		del self._SgmttnCrit
		self._SgmttnCrit = base_types.UninitialisedField(self, 'SgmttnCrit', NonEquitySubClassSegmentationCriterion1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgmttnCrit', type=NonEquitySubClassSegmentationCriterion1, min=1, max=None, mutex_group=None, array=True),
	))