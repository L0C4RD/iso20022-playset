# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralProposalResponse1Code
from . import CollateralResponse3
from . import Max35Text

class CollateralProposalResponseType4(base_types._BaseFieldType):

	__slots__ = ["_CollPrpslId", "_Rspn", "_Tp"]
	@property
	def CollPrpslId(self):
		return self._CollPrpslId

	@CollPrpslId.setter
	def CollPrpslId(self, value):
		self._CollPrpslId = value if value is not None else base_types.UninitialisedField(self, 'CollPrpslId', Max35Text, False)

	@CollPrpslId.deleter
	def CollPrpslId(self):
		del self._CollPrpslId
		self._CollPrpslId = base_types.UninitialisedField(self, 'CollPrpslId', Max35Text, False)

	@property
	def Rspn(self):
		return self._Rspn

	@Rspn.setter
	def Rspn(self, value):
		self._Rspn = value if value is not None else base_types.UninitialisedField(self, 'Rspn', CollateralResponse3, False)

	@Rspn.deleter
	def Rspn(self):
		del self._Rspn
		self._Rspn = base_types.UninitialisedField(self, 'Rspn', CollateralResponse3, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', CollateralProposalResponse1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', CollateralProposalResponse1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CollPrpslId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspn', type=CollateralResponse3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CollateralProposalResponse1Code, min=1, max=1, mutex_group=None, array=False),
	))