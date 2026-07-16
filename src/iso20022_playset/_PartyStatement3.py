# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import PartyReferenceDataChange3

class PartyStatement3(base_types._BaseFieldType):

	__slots__ = ["_Chng", "_SysDt"]
	@property
	def Chng(self):
		return self._Chng

	@Chng.setter
	def Chng(self, value):
		self._Chng = value if value is not None else base_types.UninitialisedField(self, 'Chng', PartyReferenceDataChange3, True)

	@Chng.deleter
	def Chng(self):
		del self._Chng
		self._Chng = base_types.UninitialisedField(self, 'Chng', PartyReferenceDataChange3, True)

	@property
	def SysDt(self):
		return self._SysDt

	@SysDt.setter
	def SysDt(self, value):
		self._SysDt = value if value is not None else base_types.UninitialisedField(self, 'SysDt', ISODate, False)

	@SysDt.deleter
	def SysDt(self):
		del self._SysDt
		self._SysDt = base_types.UninitialisedField(self, 'SysDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Chng', type=PartyReferenceDataChange3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SysDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))