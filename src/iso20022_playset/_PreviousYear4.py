# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PreviousYear1Choice
from . import YesNoIndicator

class PreviousYear4(base_types._BaseFieldType):

	__slots__ = ["_CshCmpntInd", "_PrvsYrs"]
	@property
	def CshCmpntInd(self):
		return self._CshCmpntInd

	@CshCmpntInd.setter
	def CshCmpntInd(self, value):
		self._CshCmpntInd = value if value is not None else base_types.UninitialisedField(self, 'CshCmpntInd', YesNoIndicator, False)

	@CshCmpntInd.deleter
	def CshCmpntInd(self):
		del self._CshCmpntInd
		self._CshCmpntInd = base_types.UninitialisedField(self, 'CshCmpntInd', YesNoIndicator, False)

	@property
	def PrvsYrs(self):
		return self._PrvsYrs

	@PrvsYrs.setter
	def PrvsYrs(self, value):
		self._PrvsYrs = value if value is not None else base_types.UninitialisedField(self, 'PrvsYrs', PreviousYear1Choice, False)

	@PrvsYrs.deleter
	def PrvsYrs(self):
		del self._PrvsYrs
		self._PrvsYrs = base_types.UninitialisedField(self, 'PrvsYrs', PreviousYear1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshCmpntInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsYrs', type=PreviousYear1Choice, min=1, max=1, mutex_group=None, array=False),
	))