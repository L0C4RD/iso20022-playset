# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import SupplementaryData1
from . import YesNoIndicator

class InformationRequestStatusChangeNotificationV01(base_types._BaseFieldType):

	__slots__ = ["_CnfdtltySts", "_OrgnlBizQry", "_SplmtryData"]
	@property
	def CnfdtltySts(self):
		return self._CnfdtltySts

	@CnfdtltySts.setter
	def CnfdtltySts(self, value):
		self._CnfdtltySts = value if value is not None else base_types.UninitialisedField(self, 'CnfdtltySts', YesNoIndicator, False)

	@CnfdtltySts.deleter
	def CnfdtltySts(self):
		del self._CnfdtltySts
		self._CnfdtltySts = base_types.UninitialisedField(self, 'CnfdtltySts', YesNoIndicator, False)

	@property
	def OrgnlBizQry(self):
		return self._OrgnlBizQry

	@OrgnlBizQry.setter
	def OrgnlBizQry(self, value):
		self._OrgnlBizQry = value if value is not None else base_types.UninitialisedField(self, 'OrgnlBizQry', Max35Text, False)

	@OrgnlBizQry.deleter
	def OrgnlBizQry(self):
		del self._OrgnlBizQry
		self._OrgnlBizQry = base_types.UninitialisedField(self, 'OrgnlBizQry', Max35Text, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CnfdtltySts', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlBizQry', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))