import base_types
import QuantityBreakdown69
import CashAccountIdentification6Choice
import SafeKeepingPlace4
import RestrictedFINXMax210Text
import PartyIdentification156

class QuantityAndAccount111(base_types._BaseFieldType):

	__slots__ = ["_QtyBrkdwn", "_DnmtnChc", "_SfkpgPlc", "_CshAcct", "_AcctOwnr"]
	@property
	def QtyBrkdwn(self):
		return self._QtyBrkdwn

	@QtyBrkdwn.setter
	def QtyBrkdwn(self, value):
		self._QtyBrkdwn = value if type(value) != auto else self.make_default("QtyBrkdwn")

	@QtyBrkdwn.deleter
	def QtyBrkdwn(self):
		del self._QtyBrkdwn
		self._QtyBrkdwn = None

	@property
	def DnmtnChc(self):
		return self._DnmtnChc

	@DnmtnChc.setter
	def DnmtnChc(self, value):
		self._DnmtnChc = value if type(value) != auto else self.make_default("DnmtnChc")

	@DnmtnChc.deleter
	def DnmtnChc(self):
		del self._DnmtnChc
		self._DnmtnChc = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtyBrkdwn', type=QuantityBreakdown69, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DnmtnChc', type=RestrictedFINXMax210Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafeKeepingPlace4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=CashAccountIdentification6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification156, min=0, max=1, mutex_group=None, array=False),
	))

