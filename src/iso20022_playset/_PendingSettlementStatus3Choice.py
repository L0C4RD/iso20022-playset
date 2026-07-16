# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Extended350Code
from . import GenericIdentification1
from . import NoReasonCode
from . import PendingSettlementStatusReason2Code

class PendingSettlementStatus3Choice(base_types._BaseFieldType):

	__slots__ = ["_DataSrcSchme", "_NoSpcfdRsn", "_Rsn", "_XtndedRsn"]
	@property
	def DataSrcSchme(self):
		return self._DataSrcSchme

	@DataSrcSchme.setter
	def DataSrcSchme(self, value):
		self._DataSrcSchme = value if value is not None else base_types.UninitialisedField(self, 'DataSrcSchme', GenericIdentification1, False)

	@DataSrcSchme.deleter
	def DataSrcSchme(self):
		del self._DataSrcSchme
		self._DataSrcSchme = base_types.UninitialisedField(self, 'DataSrcSchme', GenericIdentification1, False)

	@property
	def NoSpcfdRsn(self):
		return self._NoSpcfdRsn

	@NoSpcfdRsn.setter
	def NoSpcfdRsn(self, value):
		self._NoSpcfdRsn = value if value is not None else base_types.UninitialisedField(self, 'NoSpcfdRsn', NoReasonCode, False)

	@NoSpcfdRsn.deleter
	def NoSpcfdRsn(self):
		del self._NoSpcfdRsn
		self._NoSpcfdRsn = base_types.UninitialisedField(self, 'NoSpcfdRsn', NoReasonCode, False)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', PendingSettlementStatusReason2Code, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', PendingSettlementStatusReason2Code, False)

	@property
	def XtndedRsn(self):
		return self._XtndedRsn

	@XtndedRsn.setter
	def XtndedRsn(self, value):
		self._XtndedRsn = value if value is not None else base_types.UninitialisedField(self, 'XtndedRsn', Extended350Code, False)

	@XtndedRsn.deleter
	def XtndedRsn(self):
		del self._XtndedRsn
		self._XtndedRsn = base_types.UninitialisedField(self, 'XtndedRsn', Extended350Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataSrcSchme', type=GenericIdentification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NoSpcfdRsn', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rsn', type=PendingSettlementStatusReason2Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XtndedRsn', type=Extended350Code, min=0, max=1, mutex_group=1, array=False),
	))