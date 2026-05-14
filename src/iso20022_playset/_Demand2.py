# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._ISODateTime import ISODateTime
from ._Max2000Text import Max2000Text
from ._Max35Text import Max35Text

class Demand2(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Amt", "_Id", "_SubmissnDtTm"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def SubmissnDtTm(self):
		return self._SubmissnDtTm

	@SubmissnDtTm.setter
	def SubmissnDtTm(self, value):
		self._SubmissnDtTm = value if type(value) != base_types.auto else self.make_default("SubmissnDtTm")

	@SubmissnDtTm.deleter
	def SubmissnDtTm(self):
		del self._SubmissnDtTm
		self._SubmissnDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max2000Text, min=0, max=5, mutex_group=None, array=True),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubmissnDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))