# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import MasterAgreement7
from . import Max52Text

class LoanData120(base_types._BaseFieldType):

	__slots__ = ["_EvtDt", "_MstrAgrmt", "_UnqTradIdr"]
	@property
	def EvtDt(self):
		return self._EvtDt

	@EvtDt.setter
	def EvtDt(self, value):
		self._EvtDt = value if value is not None else base_types.UninitialisedField(self, 'EvtDt', ISODate, False)

	@EvtDt.deleter
	def EvtDt(self):
		del self._EvtDt
		self._EvtDt = base_types.UninitialisedField(self, 'EvtDt', ISODate, False)

	@property
	def MstrAgrmt(self):
		return self._MstrAgrmt

	@MstrAgrmt.setter
	def MstrAgrmt(self, value):
		self._MstrAgrmt = value if value is not None else base_types.UninitialisedField(self, 'MstrAgrmt', MasterAgreement7, False)

	@MstrAgrmt.deleter
	def MstrAgrmt(self):
		del self._MstrAgrmt
		self._MstrAgrmt = base_types.UninitialisedField(self, 'MstrAgrmt', MasterAgreement7, False)

	@property
	def UnqTradIdr(self):
		return self._UnqTradIdr

	@UnqTradIdr.setter
	def UnqTradIdr(self, value):
		self._UnqTradIdr = value if value is not None else base_types.UninitialisedField(self, 'UnqTradIdr', Max52Text, False)

	@UnqTradIdr.deleter
	def UnqTradIdr(self):
		del self._UnqTradIdr
		self._UnqTradIdr = base_types.UninitialisedField(self, 'UnqTradIdr', Max52Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EvtDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrAgrmt', type=MasterAgreement7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqTradIdr', type=Max52Text, min=0, max=1, mutex_group=None, array=False),
	))