# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Activity1
from . import BICIdentification1
from . import ISODateTime

class ActivityDetails1(base_types._BaseFieldType):

	__slots__ = ["_Actvty", "_DtTm", "_Initr"]
	@property
	def Actvty(self):
		return self._Actvty

	@Actvty.setter
	def Actvty(self, value):
		self._Actvty = value if value is not None else base_types.UninitialisedField(self, 'Actvty', Activity1, False)

	@Actvty.deleter
	def Actvty(self):
		del self._Actvty
		self._Actvty = base_types.UninitialisedField(self, 'Actvty', Activity1, False)

	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if value is not None else base_types.UninitialisedField(self, 'DtTm', ISODateTime, False)

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = base_types.UninitialisedField(self, 'DtTm', ISODateTime, False)

	@property
	def Initr(self):
		return self._Initr

	@Initr.setter
	def Initr(self, value):
		self._Initr = value if value is not None else base_types.UninitialisedField(self, 'Initr', BICIdentification1, False)

	@Initr.deleter
	def Initr(self):
		del self._Initr
		self._Initr = base_types.UninitialisedField(self, 'Initr', BICIdentification1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actvty', type=Activity1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Initr', type=BICIdentification1, min=1, max=1, mutex_group=None, array=False),
	))