# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification289

class CorporateActionAgent2(base_types._BaseFieldType):

	__slots__ = ["_InfAgt", "_Issr", "_IssrAgt", "_PngAgt", "_RedAgt", "_Regar", "_RmktgAgt", "_SlctnAgt", "_TrfAgt"]
	@property
	def InfAgt(self):
		return self._InfAgt

	@InfAgt.setter
	def InfAgt(self, value):
		self._InfAgt = value if value is not None else base_types.UninitialisedField(self, 'InfAgt', PartyIdentification289, False)

	@InfAgt.deleter
	def InfAgt(self):
		del self._InfAgt
		self._InfAgt = base_types.UninitialisedField(self, 'InfAgt', PartyIdentification289, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', PartyIdentification289, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', PartyIdentification289, False)

	@property
	def IssrAgt(self):
		return self._IssrAgt

	@IssrAgt.setter
	def IssrAgt(self, value):
		self._IssrAgt = value if value is not None else base_types.UninitialisedField(self, 'IssrAgt', PartyIdentification289, False)

	@IssrAgt.deleter
	def IssrAgt(self):
		del self._IssrAgt
		self._IssrAgt = base_types.UninitialisedField(self, 'IssrAgt', PartyIdentification289, False)

	@property
	def PngAgt(self):
		return self._PngAgt

	@PngAgt.setter
	def PngAgt(self, value):
		self._PngAgt = value if value is not None else base_types.UninitialisedField(self, 'PngAgt', PartyIdentification289, False)

	@PngAgt.deleter
	def PngAgt(self):
		del self._PngAgt
		self._PngAgt = base_types.UninitialisedField(self, 'PngAgt', PartyIdentification289, False)

	@property
	def RedAgt(self):
		return self._RedAgt

	@RedAgt.setter
	def RedAgt(self, value):
		self._RedAgt = value if value is not None else base_types.UninitialisedField(self, 'RedAgt', PartyIdentification289, False)

	@RedAgt.deleter
	def RedAgt(self):
		del self._RedAgt
		self._RedAgt = base_types.UninitialisedField(self, 'RedAgt', PartyIdentification289, False)

	@property
	def Regar(self):
		return self._Regar

	@Regar.setter
	def Regar(self, value):
		self._Regar = value if value is not None else base_types.UninitialisedField(self, 'Regar', PartyIdentification289, False)

	@Regar.deleter
	def Regar(self):
		del self._Regar
		self._Regar = base_types.UninitialisedField(self, 'Regar', PartyIdentification289, False)

	@property
	def RmktgAgt(self):
		return self._RmktgAgt

	@RmktgAgt.setter
	def RmktgAgt(self, value):
		self._RmktgAgt = value if value is not None else base_types.UninitialisedField(self, 'RmktgAgt', PartyIdentification289, False)

	@RmktgAgt.deleter
	def RmktgAgt(self):
		del self._RmktgAgt
		self._RmktgAgt = base_types.UninitialisedField(self, 'RmktgAgt', PartyIdentification289, False)

	@property
	def SlctnAgt(self):
		return self._SlctnAgt

	@SlctnAgt.setter
	def SlctnAgt(self, value):
		self._SlctnAgt = value if value is not None else base_types.UninitialisedField(self, 'SlctnAgt', PartyIdentification289, False)

	@SlctnAgt.deleter
	def SlctnAgt(self):
		del self._SlctnAgt
		self._SlctnAgt = base_types.UninitialisedField(self, 'SlctnAgt', PartyIdentification289, False)

	@property
	def TrfAgt(self):
		return self._TrfAgt

	@TrfAgt.setter
	def TrfAgt(self, value):
		self._TrfAgt = value if value is not None else base_types.UninitialisedField(self, 'TrfAgt', PartyIdentification289, False)

	@TrfAgt.deleter
	def TrfAgt(self):
		del self._TrfAgt
		self._TrfAgt = base_types.UninitialisedField(self, 'TrfAgt', PartyIdentification289, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InfAgt', type=PartyIdentification289, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=PartyIdentification289, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrAgt', type=PartyIdentification289, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PngAgt', type=PartyIdentification289, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedAgt', type=PartyIdentification289, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Regar', type=PartyIdentification289, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmktgAgt', type=PartyIdentification289, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SlctnAgt', type=PartyIdentification289, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrfAgt', type=PartyIdentification289, min=0, max=1, mutex_group=None, array=False),
	))