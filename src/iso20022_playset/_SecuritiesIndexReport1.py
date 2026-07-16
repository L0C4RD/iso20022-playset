# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import FinancialInstrument46Choice
from . import Max35Text
from . import Period4Choice

class SecuritiesIndexReport1(base_types._BaseFieldType):

	__slots__ = ["_Indx", "_RqstngNtty", "_TechRcrdId", "_VldtyPrd"]
	@property
	def Indx(self):
		return self._Indx

	@Indx.setter
	def Indx(self, value):
		self._Indx = value if value is not None else base_types.UninitialisedField(self, 'Indx', FinancialInstrument46Choice, False)

	@Indx.deleter
	def Indx(self):
		del self._Indx
		self._Indx = base_types.UninitialisedField(self, 'Indx', FinancialInstrument46Choice, False)

	@property
	def RqstngNtty(self):
		return self._RqstngNtty

	@RqstngNtty.setter
	def RqstngNtty(self, value):
		self._RqstngNtty = value if value is not None else base_types.UninitialisedField(self, 'RqstngNtty', CountryCode, False)

	@RqstngNtty.deleter
	def RqstngNtty(self):
		del self._RqstngNtty
		self._RqstngNtty = base_types.UninitialisedField(self, 'RqstngNtty', CountryCode, False)

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if value is not None else base_types.UninitialisedField(self, 'TechRcrdId', Max35Text, False)

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = base_types.UninitialisedField(self, 'TechRcrdId', Max35Text, False)

	@property
	def VldtyPrd(self):
		return self._VldtyPrd

	@VldtyPrd.setter
	def VldtyPrd(self, value):
		self._VldtyPrd = value if value is not None else base_types.UninitialisedField(self, 'VldtyPrd', Period4Choice, False)

	@VldtyPrd.deleter
	def VldtyPrd(self):
		del self._VldtyPrd
		self._VldtyPrd = base_types.UninitialisedField(self, 'VldtyPrd', Period4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Indx', type=FinancialInstrument46Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RqstngNtty', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtyPrd', type=Period4Choice, min=0, max=1, mutex_group=None, array=False),
	))