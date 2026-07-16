# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Address2
from . import ContactBusiness1
from . import Max20KText
from . import Max35Text
from . import OutputFormat4Code
from . import PartyType19Code
from . import UserInterface8Code

class RetrievalFulfilmentInstructions3(base_types._BaseFieldType):

	__slots__ = ["_ActlDlvryMtd", "_Ctct", "_EstblishdMtd", "_Frmt", "_PstlAdr", "_Rcpt", "_ReqdMtd", "_Tp", "_Trgt", "_Val"]
	@property
	def ActlDlvryMtd(self):
		return self._ActlDlvryMtd

	@ActlDlvryMtd.setter
	def ActlDlvryMtd(self, value):
		self._ActlDlvryMtd = value if value is not None else base_types.UninitialisedField(self, 'ActlDlvryMtd', Max35Text, False)

	@ActlDlvryMtd.deleter
	def ActlDlvryMtd(self):
		del self._ActlDlvryMtd
		self._ActlDlvryMtd = base_types.UninitialisedField(self, 'ActlDlvryMtd', Max35Text, False)

	@property
	def Ctct(self):
		return self._Ctct

	@Ctct.setter
	def Ctct(self, value):
		self._Ctct = value if value is not None else base_types.UninitialisedField(self, 'Ctct', ContactBusiness1, False)

	@Ctct.deleter
	def Ctct(self):
		del self._Ctct
		self._Ctct = base_types.UninitialisedField(self, 'Ctct', ContactBusiness1, False)

	@property
	def EstblishdMtd(self):
		return self._EstblishdMtd

	@EstblishdMtd.setter
	def EstblishdMtd(self, value):
		self._EstblishdMtd = value if value is not None else base_types.UninitialisedField(self, 'EstblishdMtd', Max35Text, True)

	@EstblishdMtd.deleter
	def EstblishdMtd(self):
		del self._EstblishdMtd
		self._EstblishdMtd = base_types.UninitialisedField(self, 'EstblishdMtd', Max35Text, True)

	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if value is not None else base_types.UninitialisedField(self, 'Frmt', OutputFormat4Code, False)

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = base_types.UninitialisedField(self, 'Frmt', OutputFormat4Code, False)

	@property
	def PstlAdr(self):
		return self._PstlAdr

	@PstlAdr.setter
	def PstlAdr(self, value):
		self._PstlAdr = value if value is not None else base_types.UninitialisedField(self, 'PstlAdr', Address2, False)

	@PstlAdr.deleter
	def PstlAdr(self):
		del self._PstlAdr
		self._PstlAdr = base_types.UninitialisedField(self, 'PstlAdr', Address2, False)

	@property
	def Rcpt(self):
		return self._Rcpt

	@Rcpt.setter
	def Rcpt(self, value):
		self._Rcpt = value if value is not None else base_types.UninitialisedField(self, 'Rcpt', PartyType19Code, False)

	@Rcpt.deleter
	def Rcpt(self):
		del self._Rcpt
		self._Rcpt = base_types.UninitialisedField(self, 'Rcpt', PartyType19Code, False)

	@property
	def ReqdMtd(self):
		return self._ReqdMtd

	@ReqdMtd.setter
	def ReqdMtd(self, value):
		self._ReqdMtd = value if value is not None else base_types.UninitialisedField(self, 'ReqdMtd', Max35Text, True)

	@ReqdMtd.deleter
	def ReqdMtd(self):
		del self._ReqdMtd
		self._ReqdMtd = base_types.UninitialisedField(self, 'ReqdMtd', Max35Text, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@property
	def Trgt(self):
		return self._Trgt

	@Trgt.setter
	def Trgt(self, value):
		self._Trgt = value if value is not None else base_types.UninitialisedField(self, 'Trgt', UserInterface8Code, True)

	@Trgt.deleter
	def Trgt(self):
		del self._Trgt
		self._Trgt = base_types.UninitialisedField(self, 'Trgt', UserInterface8Code, True)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', Max20KText, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', Max20KText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActlDlvryMtd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctct', type=ContactBusiness1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstblishdMtd', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Frmt', type=OutputFormat4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlAdr', type=Address2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rcpt', type=PartyType19Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdMtd', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Trgt', type=UserInterface8Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Val', type=Max20KText, min=1, max=1, mutex_group=None, array=False),
	))