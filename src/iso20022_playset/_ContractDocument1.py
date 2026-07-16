# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Max35Text
from . import Max6Text

class ContractDocument1(base_types._BaseFieldType):

	__slots__ = ["_Ref", "_SgnOffDt", "_Vrsn"]
	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@property
	def SgnOffDt(self):
		return self._SgnOffDt

	@SgnOffDt.setter
	def SgnOffDt(self, value):
		self._SgnOffDt = value if value is not None else base_types.UninitialisedField(self, 'SgnOffDt', ISODate, False)

	@SgnOffDt.deleter
	def SgnOffDt(self):
		del self._SgnOffDt
		self._SgnOffDt = base_types.UninitialisedField(self, 'SgnOffDt', ISODate, False)

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', Max6Text, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', Max6Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ref', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgnOffDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Max6Text, min=0, max=1, mutex_group=None, array=False),
	))