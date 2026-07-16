# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Adjustment13
from . import LoyaltyProgramme4
from . import Max35Text
from . import SaleItem5

class Sale4(base_types._BaseFieldType):

	__slots__ = ["_Adjstmnt", "_LineItm", "_LltyPrgrmm", "_SummryCmmdtyId"]
	@property
	def Adjstmnt(self):
		return self._Adjstmnt

	@Adjstmnt.setter
	def Adjstmnt(self, value):
		self._Adjstmnt = value if value is not None else base_types.UninitialisedField(self, 'Adjstmnt', Adjustment13, True)

	@Adjstmnt.deleter
	def Adjstmnt(self):
		del self._Adjstmnt
		self._Adjstmnt = base_types.UninitialisedField(self, 'Adjstmnt', Adjustment13, True)

	@property
	def LineItm(self):
		return self._LineItm

	@LineItm.setter
	def LineItm(self, value):
		self._LineItm = value if value is not None else base_types.UninitialisedField(self, 'LineItm', SaleItem5, True)

	@LineItm.deleter
	def LineItm(self):
		del self._LineItm
		self._LineItm = base_types.UninitialisedField(self, 'LineItm', SaleItem5, True)

	@property
	def LltyPrgrmm(self):
		return self._LltyPrgrmm

	@LltyPrgrmm.setter
	def LltyPrgrmm(self, value):
		self._LltyPrgrmm = value if value is not None else base_types.UninitialisedField(self, 'LltyPrgrmm', LoyaltyProgramme4, False)

	@LltyPrgrmm.deleter
	def LltyPrgrmm(self):
		del self._LltyPrgrmm
		self._LltyPrgrmm = base_types.UninitialisedField(self, 'LltyPrgrmm', LoyaltyProgramme4, False)

	@property
	def SummryCmmdtyId(self):
		return self._SummryCmmdtyId

	@SummryCmmdtyId.setter
	def SummryCmmdtyId(self, value):
		self._SummryCmmdtyId = value if value is not None else base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	@SummryCmmdtyId.deleter
	def SummryCmmdtyId(self):
		del self._SummryCmmdtyId
		self._SummryCmmdtyId = base_types.UninitialisedField(self, 'SummryCmmdtyId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adjstmnt', type=Adjustment13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LineItm', type=SaleItem5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LltyPrgrmm', type=LoyaltyProgramme4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SummryCmmdtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))