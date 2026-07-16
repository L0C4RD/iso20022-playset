# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CashAccountIdentification9Choice
from . import Max210Text
from . import PartyIdentification144
from . import QuantityBreakdown62
from . import SafeKeepingPlace5

class QuantityAndAccount118(base_types._BaseFieldType):

	__slots__ = ["_AcctOwnr", "_CshAcct", "_DnmtnChc", "_QtyBrkdwn", "_SfkpgPlc"]
	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification144, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification144, False)

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if value is not None else base_types.UninitialisedField(self, 'CshAcct', CashAccountIdentification9Choice, False)

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = base_types.UninitialisedField(self, 'CshAcct', CashAccountIdentification9Choice, False)

	@property
	def DnmtnChc(self):
		return self._DnmtnChc

	@DnmtnChc.setter
	def DnmtnChc(self, value):
		self._DnmtnChc = value if value is not None else base_types.UninitialisedField(self, 'DnmtnChc', Max210Text, False)

	@DnmtnChc.deleter
	def DnmtnChc(self):
		del self._DnmtnChc
		self._DnmtnChc = base_types.UninitialisedField(self, 'DnmtnChc', Max210Text, False)

	@property
	def QtyBrkdwn(self):
		return self._QtyBrkdwn

	@QtyBrkdwn.setter
	def QtyBrkdwn(self, value):
		self._QtyBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'QtyBrkdwn', QuantityBreakdown62, True)

	@QtyBrkdwn.deleter
	def QtyBrkdwn(self):
		del self._QtyBrkdwn
		self._QtyBrkdwn = base_types.UninitialisedField(self, 'QtyBrkdwn', QuantityBreakdown62, True)

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafeKeepingPlace5, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafeKeepingPlace5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification144, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification9Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DnmtnChc', type=Max210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown62, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace5, min=0, max=1, mutex_group=None, array=False),
	))