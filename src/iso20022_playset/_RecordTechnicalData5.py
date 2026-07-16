# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExternalAuthorityExchangeReason1Code
from . import ISODateTime

class RecordTechnicalData5(base_types._BaseFieldType):

	__slots__ = ["_RctDtTm", "_XchgRsn"]
	@property
	def RctDtTm(self):
		return self._RctDtTm

	@RctDtTm.setter
	def RctDtTm(self, value):
		self._RctDtTm = value if value is not None else base_types.UninitialisedField(self, 'RctDtTm', ISODateTime, False)

	@RctDtTm.deleter
	def RctDtTm(self):
		del self._RctDtTm
		self._RctDtTm = base_types.UninitialisedField(self, 'RctDtTm', ISODateTime, False)

	@property
	def XchgRsn(self):
		return self._XchgRsn

	@XchgRsn.setter
	def XchgRsn(self, value):
		self._XchgRsn = value if value is not None else base_types.UninitialisedField(self, 'XchgRsn', ExternalAuthorityExchangeReason1Code, True)

	@XchgRsn.deleter
	def XchgRsn(self):
		del self._XchgRsn
		self._XchgRsn = base_types.UninitialisedField(self, 'XchgRsn', ExternalAuthorityExchangeReason1Code, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RctDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRsn', type=ExternalAuthorityExchangeReason1Code, min=1, max=None, mutex_group=None, array=True),
	))