# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import DerivativePartyIdentification1Choice
from . import TrueFalseIndicator

class CreditDefaultSwapSingleName2(base_types._BaseFieldType):

	__slots__ = ["_NtnlCcy", "_RefPty", "_SvrgnIssr"]
	@property
	def NtnlCcy(self):
		return self._NtnlCcy

	@NtnlCcy.setter
	def NtnlCcy(self, value):
		self._NtnlCcy = value if value is not None else base_types.UninitialisedField(self, 'NtnlCcy', ActiveOrHistoricCurrencyCode, False)

	@NtnlCcy.deleter
	def NtnlCcy(self):
		del self._NtnlCcy
		self._NtnlCcy = base_types.UninitialisedField(self, 'NtnlCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def RefPty(self):
		return self._RefPty

	@RefPty.setter
	def RefPty(self, value):
		self._RefPty = value if value is not None else base_types.UninitialisedField(self, 'RefPty', DerivativePartyIdentification1Choice, False)

	@RefPty.deleter
	def RefPty(self):
		del self._RefPty
		self._RefPty = base_types.UninitialisedField(self, 'RefPty', DerivativePartyIdentification1Choice, False)

	@property
	def SvrgnIssr(self):
		return self._SvrgnIssr

	@SvrgnIssr.setter
	def SvrgnIssr(self, value):
		self._SvrgnIssr = value if value is not None else base_types.UninitialisedField(self, 'SvrgnIssr', TrueFalseIndicator, False)

	@SvrgnIssr.deleter
	def SvrgnIssr(self):
		del self._SvrgnIssr
		self._SvrgnIssr = base_types.UninitialisedField(self, 'SvrgnIssr', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NtnlCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefPty', type=DerivativePartyIdentification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvrgnIssr', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
	))