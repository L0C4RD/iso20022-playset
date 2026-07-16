# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DocumentAdjustment1
from . import DocumentAmount1

class RemittanceAmount4(base_types._BaseFieldType):

	__slots__ = ["_AdjstmntAmtAndRsn", "_RmtAmtAndTp"]
	@property
	def AdjstmntAmtAndRsn(self):
		return self._AdjstmntAmtAndRsn

	@AdjstmntAmtAndRsn.setter
	def AdjstmntAmtAndRsn(self, value):
		self._AdjstmntAmtAndRsn = value if value is not None else base_types.UninitialisedField(self, 'AdjstmntAmtAndRsn', DocumentAdjustment1, True)

	@AdjstmntAmtAndRsn.deleter
	def AdjstmntAmtAndRsn(self):
		del self._AdjstmntAmtAndRsn
		self._AdjstmntAmtAndRsn = base_types.UninitialisedField(self, 'AdjstmntAmtAndRsn', DocumentAdjustment1, True)

	@property
	def RmtAmtAndTp(self):
		return self._RmtAmtAndTp

	@RmtAmtAndTp.setter
	def RmtAmtAndTp(self, value):
		self._RmtAmtAndTp = value if value is not None else base_types.UninitialisedField(self, 'RmtAmtAndTp', DocumentAmount1, True)

	@RmtAmtAndTp.deleter
	def RmtAmtAndTp(self):
		del self._RmtAmtAndTp
		self._RmtAmtAndTp = base_types.UninitialisedField(self, 'RmtAmtAndTp', DocumentAmount1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdjstmntAmtAndRsn', type=DocumentAdjustment1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RmtAmtAndTp', type=DocumentAmount1, min=0, max=None, mutex_group=None, array=True),
	))