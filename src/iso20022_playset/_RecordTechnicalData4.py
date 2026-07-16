# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import ISODateTime
from . import MICIdentifier
from . import Period4Choice
from . import TrueFalseIndicator

class RecordTechnicalData4(base_types._BaseFieldType):

	__slots__ = ["_IncnsstncyInd", "_LastUpd", "_NvrPblshd", "_PblctnPrd", "_RlvntCmptntAuthrty", "_RlvntTradgVn", "_SubmissnDtTm"]
	@property
	def IncnsstncyInd(self):
		return self._IncnsstncyInd

	@IncnsstncyInd.setter
	def IncnsstncyInd(self, value):
		self._IncnsstncyInd = value if value is not None else base_types.UninitialisedField(self, 'IncnsstncyInd', TrueFalseIndicator, False)

	@IncnsstncyInd.deleter
	def IncnsstncyInd(self):
		del self._IncnsstncyInd
		self._IncnsstncyInd = base_types.UninitialisedField(self, 'IncnsstncyInd', TrueFalseIndicator, False)

	@property
	def LastUpd(self):
		return self._LastUpd

	@LastUpd.setter
	def LastUpd(self, value):
		self._LastUpd = value if value is not None else base_types.UninitialisedField(self, 'LastUpd', ISODateTime, False)

	@LastUpd.deleter
	def LastUpd(self):
		del self._LastUpd
		self._LastUpd = base_types.UninitialisedField(self, 'LastUpd', ISODateTime, False)

	@property
	def NvrPblshd(self):
		return self._NvrPblshd

	@NvrPblshd.setter
	def NvrPblshd(self, value):
		self._NvrPblshd = value if value is not None else base_types.UninitialisedField(self, 'NvrPblshd', TrueFalseIndicator, False)

	@NvrPblshd.deleter
	def NvrPblshd(self):
		del self._NvrPblshd
		self._NvrPblshd = base_types.UninitialisedField(self, 'NvrPblshd', TrueFalseIndicator, False)

	@property
	def PblctnPrd(self):
		return self._PblctnPrd

	@PblctnPrd.setter
	def PblctnPrd(self, value):
		self._PblctnPrd = value if value is not None else base_types.UninitialisedField(self, 'PblctnPrd', Period4Choice, False)

	@PblctnPrd.deleter
	def PblctnPrd(self):
		del self._PblctnPrd
		self._PblctnPrd = base_types.UninitialisedField(self, 'PblctnPrd', Period4Choice, False)

	@property
	def RlvntCmptntAuthrty(self):
		return self._RlvntCmptntAuthrty

	@RlvntCmptntAuthrty.setter
	def RlvntCmptntAuthrty(self, value):
		self._RlvntCmptntAuthrty = value if value is not None else base_types.UninitialisedField(self, 'RlvntCmptntAuthrty', CountryCode, False)

	@RlvntCmptntAuthrty.deleter
	def RlvntCmptntAuthrty(self):
		del self._RlvntCmptntAuthrty
		self._RlvntCmptntAuthrty = base_types.UninitialisedField(self, 'RlvntCmptntAuthrty', CountryCode, False)

	@property
	def RlvntTradgVn(self):
		return self._RlvntTradgVn

	@RlvntTradgVn.setter
	def RlvntTradgVn(self, value):
		self._RlvntTradgVn = value if value is not None else base_types.UninitialisedField(self, 'RlvntTradgVn', MICIdentifier, False)

	@RlvntTradgVn.deleter
	def RlvntTradgVn(self):
		del self._RlvntTradgVn
		self._RlvntTradgVn = base_types.UninitialisedField(self, 'RlvntTradgVn', MICIdentifier, False)

	@property
	def SubmissnDtTm(self):
		return self._SubmissnDtTm

	@SubmissnDtTm.setter
	def SubmissnDtTm(self, value):
		self._SubmissnDtTm = value if value is not None else base_types.UninitialisedField(self, 'SubmissnDtTm', ISODateTime, False)

	@SubmissnDtTm.deleter
	def SubmissnDtTm(self):
		del self._SubmissnDtTm
		self._SubmissnDtTm = base_types.UninitialisedField(self, 'SubmissnDtTm', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IncnsstncyInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastUpd', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NvrPblshd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PblctnPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RlvntCmptntAuthrty', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RlvntTradgVn', type=MICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmissnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))