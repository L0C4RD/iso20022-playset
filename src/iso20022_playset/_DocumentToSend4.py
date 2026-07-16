# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CommunicationMethod3Choice
from . import Max140Text
from . import PartyIdentification125Choice

class DocumentToSend4(base_types._BaseFieldType):

	__slots__ = ["_MtdOfTrnsmssn", "_Rcpt", "_Tp"]
	@property
	def MtdOfTrnsmssn(self):
		return self._MtdOfTrnsmssn

	@MtdOfTrnsmssn.setter
	def MtdOfTrnsmssn(self, value):
		self._MtdOfTrnsmssn = value if value is not None else base_types.UninitialisedField(self, 'MtdOfTrnsmssn', CommunicationMethod3Choice, False)

	@MtdOfTrnsmssn.deleter
	def MtdOfTrnsmssn(self):
		del self._MtdOfTrnsmssn
		self._MtdOfTrnsmssn = base_types.UninitialisedField(self, 'MtdOfTrnsmssn', CommunicationMethod3Choice, False)

	@property
	def Rcpt(self):
		return self._Rcpt

	@Rcpt.setter
	def Rcpt(self, value):
		self._Rcpt = value if value is not None else base_types.UninitialisedField(self, 'Rcpt', PartyIdentification125Choice, False)

	@Rcpt.deleter
	def Rcpt(self):
		del self._Rcpt
		self._Rcpt = base_types.UninitialisedField(self, 'Rcpt', PartyIdentification125Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max140Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MtdOfTrnsmssn', type=CommunicationMethod3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcpt', type=PartyIdentification125Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
	))