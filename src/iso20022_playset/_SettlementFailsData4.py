# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SettlementFailsDerogation1
from . import SettlementFailureReason3
from . import SettlementTotalData1

class SettlementFailsData4(base_types._BaseFieldType):

	__slots__ = ["_ElgblForDrgtn", "_FailrRsn", "_Ttl"]
	@property
	def ElgblForDrgtn(self):
		return self._ElgblForDrgtn

	@ElgblForDrgtn.setter
	def ElgblForDrgtn(self, value):
		self._ElgblForDrgtn = value if value is not None else base_types.UninitialisedField(self, 'ElgblForDrgtn', SettlementFailsDerogation1, False)

	@ElgblForDrgtn.deleter
	def ElgblForDrgtn(self):
		del self._ElgblForDrgtn
		self._ElgblForDrgtn = base_types.UninitialisedField(self, 'ElgblForDrgtn', SettlementFailsDerogation1, False)

	@property
	def FailrRsn(self):
		return self._FailrRsn

	@FailrRsn.setter
	def FailrRsn(self, value):
		self._FailrRsn = value if value is not None else base_types.UninitialisedField(self, 'FailrRsn', SettlementFailureReason3, False)

	@FailrRsn.deleter
	def FailrRsn(self):
		del self._FailrRsn
		self._FailrRsn = base_types.UninitialisedField(self, 'FailrRsn', SettlementFailureReason3, False)

	@property
	def Ttl(self):
		return self._Ttl

	@Ttl.setter
	def Ttl(self, value):
		self._Ttl = value if value is not None else base_types.UninitialisedField(self, 'Ttl', SettlementTotalData1, False)

	@Ttl.deleter
	def Ttl(self):
		del self._Ttl
		self._Ttl = base_types.UninitialisedField(self, 'Ttl', SettlementTotalData1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElgblForDrgtn', type=SettlementFailsDerogation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FailrRsn', type=SettlementFailureReason3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ttl', type=SettlementTotalData1, min=1, max=1, mutex_group=None, array=False),
	))