# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import ReturnExcessCash1Choice

class ReturnExcessCash1(base_types._BaseFieldType):

	__slots__ = ["_CshCollCcy", "_RtrXcssCshTp"]
	@property
	def CshCollCcy(self):
		return self._CshCollCcy

	@CshCollCcy.setter
	def CshCollCcy(self, value):
		self._CshCollCcy = value if value is not None else base_types.UninitialisedField(self, 'CshCollCcy', ActiveOrHistoricCurrencyCode, False)

	@CshCollCcy.deleter
	def CshCollCcy(self):
		del self._CshCollCcy
		self._CshCollCcy = base_types.UninitialisedField(self, 'CshCollCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def RtrXcssCshTp(self):
		return self._RtrXcssCshTp

	@RtrXcssCshTp.setter
	def RtrXcssCshTp(self, value):
		self._RtrXcssCshTp = value if value is not None else base_types.UninitialisedField(self, 'RtrXcssCshTp', ReturnExcessCash1Choice, False)

	@RtrXcssCshTp.deleter
	def RtrXcssCshTp(self):
		del self._RtrXcssCshTp
		self._RtrXcssCshTp = base_types.UninitialisedField(self, 'RtrXcssCshTp', ReturnExcessCash1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CshCollCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrXcssCshTp', type=ReturnExcessCash1Choice, min=1, max=1, mutex_group=None, array=False),
	))