# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinalStatus1Code
from . import Max35Text
from . import Max4AlphaNumericText
from . import PendingStatus4Code

class PaymentStatusCode6Choice(base_types._BaseFieldType):

	__slots__ = ["_Fnl", "_Pdg", "_Prtry", "_RTGS", "_Sttlm"]
	@property
	def Fnl(self):
		return self._Fnl

	@Fnl.setter
	def Fnl(self, value):
		self._Fnl = value if value is not None else base_types.UninitialisedField(self, 'Fnl', FinalStatus1Code, False)

	@Fnl.deleter
	def Fnl(self):
		del self._Fnl
		self._Fnl = base_types.UninitialisedField(self, 'Fnl', FinalStatus1Code, False)

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if value is not None else base_types.UninitialisedField(self, 'Pdg', PendingStatus4Code, False)

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = base_types.UninitialisedField(self, 'Pdg', PendingStatus4Code, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', Max35Text, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', Max35Text, False)

	@property
	def RTGS(self):
		return self._RTGS

	@RTGS.setter
	def RTGS(self, value):
		self._RTGS = value if value is not None else base_types.UninitialisedField(self, 'RTGS', Max4AlphaNumericText, False)

	@RTGS.deleter
	def RTGS(self):
		del self._RTGS
		self._RTGS = base_types.UninitialisedField(self, 'RTGS', Max4AlphaNumericText, False)

	@property
	def Sttlm(self):
		return self._Sttlm

	@Sttlm.setter
	def Sttlm(self, value):
		self._Sttlm = value if value is not None else base_types.UninitialisedField(self, 'Sttlm', Max4AlphaNumericText, False)

	@Sttlm.deleter
	def Sttlm(self):
		del self._Sttlm
		self._Sttlm = base_types.UninitialisedField(self, 'Sttlm', Max4AlphaNumericText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Fnl', type=FinalStatus1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdg', type=PendingStatus4Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prtry', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RTGS', type=Max4AlphaNumericText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Sttlm', type=Max4AlphaNumericText, min=0, max=1, mutex_group=1, array=False),
	))