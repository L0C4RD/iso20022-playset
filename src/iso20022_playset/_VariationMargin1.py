# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import RoundingMethod1Code
from . import ThresholdType1Code

class VariationMargin1(base_types._BaseFieldType):

	__slots__ = ["_MinTrfAmt", "_RndgAmt", "_RndgMtd", "_ThrshldAmt", "_ThrshldTp"]
	@property
	def MinTrfAmt(self):
		return self._MinTrfAmt

	@MinTrfAmt.setter
	def MinTrfAmt(self, value):
		self._MinTrfAmt = value if value is not None else base_types.UninitialisedField(self, 'MinTrfAmt', ActiveCurrencyAndAmount, False)

	@MinTrfAmt.deleter
	def MinTrfAmt(self):
		del self._MinTrfAmt
		self._MinTrfAmt = base_types.UninitialisedField(self, 'MinTrfAmt', ActiveCurrencyAndAmount, False)

	@property
	def RndgAmt(self):
		return self._RndgAmt

	@RndgAmt.setter
	def RndgAmt(self, value):
		self._RndgAmt = value if value is not None else base_types.UninitialisedField(self, 'RndgAmt', ActiveCurrencyAndAmount, False)

	@RndgAmt.deleter
	def RndgAmt(self):
		del self._RndgAmt
		self._RndgAmt = base_types.UninitialisedField(self, 'RndgAmt', ActiveCurrencyAndAmount, False)

	@property
	def RndgMtd(self):
		return self._RndgMtd

	@RndgMtd.setter
	def RndgMtd(self, value):
		self._RndgMtd = value if value is not None else base_types.UninitialisedField(self, 'RndgMtd', RoundingMethod1Code, False)

	@RndgMtd.deleter
	def RndgMtd(self):
		del self._RndgMtd
		self._RndgMtd = base_types.UninitialisedField(self, 'RndgMtd', RoundingMethod1Code, False)

	@property
	def ThrshldAmt(self):
		return self._ThrshldAmt

	@ThrshldAmt.setter
	def ThrshldAmt(self, value):
		self._ThrshldAmt = value if value is not None else base_types.UninitialisedField(self, 'ThrshldAmt', ActiveCurrencyAndAmount, False)

	@ThrshldAmt.deleter
	def ThrshldAmt(self):
		del self._ThrshldAmt
		self._ThrshldAmt = base_types.UninitialisedField(self, 'ThrshldAmt', ActiveCurrencyAndAmount, False)

	@property
	def ThrshldTp(self):
		return self._ThrshldTp

	@ThrshldTp.setter
	def ThrshldTp(self, value):
		self._ThrshldTp = value if value is not None else base_types.UninitialisedField(self, 'ThrshldTp', ThresholdType1Code, False)

	@ThrshldTp.deleter
	def ThrshldTp(self):
		del self._ThrshldTp
		self._ThrshldTp = base_types.UninitialisedField(self, 'ThrshldTp', ThresholdType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MinTrfAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RndgAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RndgMtd', type=RoundingMethod1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrshldAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ThrshldTp', type=ThresholdType1Code, min=0, max=1, mutex_group=None, array=False),
	))