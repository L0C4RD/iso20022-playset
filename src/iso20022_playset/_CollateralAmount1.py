# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount

class CollateralAmount1(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrstAmt", "_CollAmt", "_FeesAndComssns", "_MktValAmt", "_RptdCcyAndAmt"]
	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstAmt', ActiveCurrencyAndAmount, False)

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = base_types.UninitialisedField(self, 'AcrdIntrstAmt', ActiveCurrencyAndAmount, False)

	@property
	def CollAmt(self):
		return self._CollAmt

	@CollAmt.setter
	def CollAmt(self, value):
		self._CollAmt = value if value is not None else base_types.UninitialisedField(self, 'CollAmt', ActiveCurrencyAndAmount, False)

	@CollAmt.deleter
	def CollAmt(self):
		del self._CollAmt
		self._CollAmt = base_types.UninitialisedField(self, 'CollAmt', ActiveCurrencyAndAmount, False)

	@property
	def FeesAndComssns(self):
		return self._FeesAndComssns

	@FeesAndComssns.setter
	def FeesAndComssns(self, value):
		self._FeesAndComssns = value if value is not None else base_types.UninitialisedField(self, 'FeesAndComssns', ActiveCurrencyAndAmount, False)

	@FeesAndComssns.deleter
	def FeesAndComssns(self):
		del self._FeesAndComssns
		self._FeesAndComssns = base_types.UninitialisedField(self, 'FeesAndComssns', ActiveCurrencyAndAmount, False)

	@property
	def MktValAmt(self):
		return self._MktValAmt

	@MktValAmt.setter
	def MktValAmt(self, value):
		self._MktValAmt = value if value is not None else base_types.UninitialisedField(self, 'MktValAmt', ActiveCurrencyAndAmount, False)

	@MktValAmt.deleter
	def MktValAmt(self):
		del self._MktValAmt
		self._MktValAmt = base_types.UninitialisedField(self, 'MktValAmt', ActiveCurrencyAndAmount, False)

	@property
	def RptdCcyAndAmt(self):
		return self._RptdCcyAndAmt

	@RptdCcyAndAmt.setter
	def RptdCcyAndAmt(self, value):
		self._RptdCcyAndAmt = value if value is not None else base_types.UninitialisedField(self, 'RptdCcyAndAmt', ActiveCurrencyAndAmount, False)

	@RptdCcyAndAmt.deleter
	def RptdCcyAndAmt(self):
		del self._RptdCcyAndAmt
		self._RptdCcyAndAmt = base_types.UninitialisedField(self, 'RptdCcyAndAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdIntrstAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FeesAndComssns', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktValAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptdCcyAndAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))