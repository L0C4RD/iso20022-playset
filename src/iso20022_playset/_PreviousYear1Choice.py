# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISOYear
from . import PreviousAll

class PreviousYear1Choice(base_types._BaseFieldType):

	__slots__ = ["_AllPrvsYrs", "_SpcfcPrvsYrs"]
	@property
	def AllPrvsYrs(self):
		return self._AllPrvsYrs

	@AllPrvsYrs.setter
	def AllPrvsYrs(self, value):
		self._AllPrvsYrs = value if value is not None else base_types.UninitialisedField(self, 'AllPrvsYrs', PreviousAll, False)

	@AllPrvsYrs.deleter
	def AllPrvsYrs(self):
		del self._AllPrvsYrs
		self._AllPrvsYrs = base_types.UninitialisedField(self, 'AllPrvsYrs', PreviousAll, False)

	@property
	def SpcfcPrvsYrs(self):
		return self._SpcfcPrvsYrs

	@SpcfcPrvsYrs.setter
	def SpcfcPrvsYrs(self, value):
		self._SpcfcPrvsYrs = value if value is not None else base_types.UninitialisedField(self, 'SpcfcPrvsYrs', ISOYear, True)

	@SpcfcPrvsYrs.deleter
	def SpcfcPrvsYrs(self):
		del self._SpcfcPrvsYrs
		self._SpcfcPrvsYrs = base_types.UninitialisedField(self, 'SpcfcPrvsYrs', ISOYear, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AllPrvsYrs', type=PreviousAll, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SpcfcPrvsYrs', type=ISOYear, min=1, max=None, mutex_group=1, array=True),
	))