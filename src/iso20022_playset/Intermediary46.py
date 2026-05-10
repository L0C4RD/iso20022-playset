import base_types
import Account32
import PartyIdentification177Choice
import YesNoIndicator
import CommunicationAddress6
import PartyRole2Choice
import LEIIdentifier
import NameAndAddress4

class Intermediary46(base_types._BaseFieldType):

	__slots__ = ["_PmryComAdr", "_ScndryComAdr", "_NmAndAdr", "_Acct", "_WvdTrlrComssnInd", "_Role", "_Id", "_LglNttyIdr"]
	@property
	def PmryComAdr(self):
		return self._PmryComAdr

	@PmryComAdr.setter
	def PmryComAdr(self, value):
		self._PmryComAdr = value if type(value) != auto else self.make_default("PmryComAdr")

	@PmryComAdr.deleter
	def PmryComAdr(self):
		del self._PmryComAdr
		self._PmryComAdr = None

	@property
	def ScndryComAdr(self):
		return self._ScndryComAdr

	@ScndryComAdr.setter
	def ScndryComAdr(self, value):
		self._ScndryComAdr = value if type(value) != auto else self.make_default("ScndryComAdr")

	@ScndryComAdr.deleter
	def ScndryComAdr(self):
		del self._ScndryComAdr
		self._ScndryComAdr = None

	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if type(value) != auto else self.make_default("NmAndAdr")

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = None

	@property
	def Acct(self):
		return self._Acct

	@Acct.setter
	def Acct(self, value):
		self._Acct = value if type(value) != auto else self.make_default("Acct")

	@Acct.deleter
	def Acct(self):
		del self._Acct
		self._Acct = None

	@property
	def WvdTrlrComssnInd(self):
		return self._WvdTrlrComssnInd

	@WvdTrlrComssnInd.setter
	def WvdTrlrComssnInd(self, value):
		self._WvdTrlrComssnInd = value if type(value) != auto else self.make_default("WvdTrlrComssnInd")

	@WvdTrlrComssnInd.deleter
	def WvdTrlrComssnInd(self):
		del self._WvdTrlrComssnInd
		self._WvdTrlrComssnInd = None

	@property
	def Role(self):
		return self._Role

	@Role.setter
	def Role(self, value):
		self._Role = value if type(value) != auto else self.make_default("Role")

	@Role.deleter
	def Role(self):
		del self._Role
		self._Role = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def LglNttyIdr(self):
		return self._LglNttyIdr

	@LglNttyIdr.setter
	def LglNttyIdr(self, value):
		self._LglNttyIdr = value if type(value) != auto else self.make_default("LglNttyIdr")

	@LglNttyIdr.deleter
	def LglNttyIdr(self):
		del self._LglNttyIdr
		self._LglNttyIdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmryComAdr', type=CommunicationAddress6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ScndryComAdr', type=CommunicationAddress6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acct', type=Account32, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WvdTrlrComssnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Role', type=PartyRole2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=PartyIdentification177Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglNttyIdr', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
	))

