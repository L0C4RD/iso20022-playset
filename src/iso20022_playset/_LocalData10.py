# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import ISOMax3ALanguageCode
from . import LocalAddress1
from . import Max35Text
from . import Max512Text
from . import Max70Text

class LocalData10(base_types._BaseFieldType):

	__slots__ = ["_AddtlCtct", "_AddtlData", "_Adr", "_Lang", "_NcodgFrmt", "_Nm"]
	@property
	def AddtlCtct(self):
		return self._AddtlCtct

	@AddtlCtct.setter
	def AddtlCtct(self, value):
		self._AddtlCtct = value if value is not None else base_types.UninitialisedField(self, 'AddtlCtct', Max512Text, False)

	@AddtlCtct.deleter
	def AddtlCtct(self):
		del self._AddtlCtct
		self._AddtlCtct = base_types.UninitialisedField(self, 'AddtlCtct', Max512Text, False)

	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', LocalAddress1, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', LocalAddress1, False)

	@property
	def Lang(self):
		return self._Lang

	@Lang.setter
	def Lang(self, value):
		self._Lang = value if value is not None else base_types.UninitialisedField(self, 'Lang', ISOMax3ALanguageCode, False)

	@Lang.deleter
	def Lang(self):
		del self._Lang
		self._Lang = base_types.UninitialisedField(self, 'Lang', ISOMax3ALanguageCode, False)

	@property
	def NcodgFrmt(self):
		return self._NcodgFrmt

	@NcodgFrmt.setter
	def NcodgFrmt(self, value):
		self._NcodgFrmt = value if value is not None else base_types.UninitialisedField(self, 'NcodgFrmt', Max35Text, False)

	@NcodgFrmt.deleter
	def NcodgFrmt(self):
		del self._NcodgFrmt
		self._NcodgFrmt = base_types.UninitialisedField(self, 'NcodgFrmt', Max35Text, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max70Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max70Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlCtct', type=Max512Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Adr', type=LocalAddress1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lang', type=ISOMax3ALanguageCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NcodgFrmt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))